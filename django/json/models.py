from django.db import models
from django.utils.encoding import smart_unicode, is_protected_type

class BaseModel(models.Model):

    def natural_key(self):
        natural = {}
        concrete_model = self._meta.concrete_model
        for field in concrete_model._meta.fields:   # local_fields and OneToOnes
            if field.rel is None:
                natural[field.name] = self.natural_field(field)
            elif not field.name.endswith('_ptr'):
                natural[field.name] = self.natural_fk_field(field)
        for field in concrete_model._meta.many_to_many:
            natural[field.name] = self.natural_m2m_field(field)
        return natural

    def natural_field(self, field):
        value = field._get_val_from_obj(self)
        if is_protected_type(value):
            return value
        else:
            return field.value_to_string(self)

    def natural_fk_field(self, field):
        if hasattr(field.rel.to, 'natural_key'):
            print field.name
            related = getattr(self, field.name)
            if related:
                return related.natural_key()
            else:
                return None
        else:
            return getattr(self, field.get_attname())

    def natural_m2m_field(self, field):
        if field.rel.through._meta.auto_created:
            if hasattr(field.rel.to, 'natural_key'):
                return [related.natural_key()
                        for related in getattr(self, field.name).iterator()]
            else:
                return [smart_unicode(related._get_pk_val(), string_only=True)
                        for related in getattr(self, field.name).iterator()]
        else:
            return None

    class Meta:
        abstract = True
