from django.contrib import admin

from .models import *


class ModelAAdmin(admin.ModelAdmin):
    pass

class InlineModelB(admin.TabularInline):
     model=ModelB
     raw_id_fields=('model_a_fk', 'model_c_fk')

class ModelBAdmin(admin.ModelAdmin):
     raw_id_fields=('model_a_fk', 'model_c_fk')

class ModelCAdmin(admin.ModelAdmin):
     inlines=(InlineModelB,)

admin.site.register(ModelA, ModelAAdmin)
admin.site.register(ModelB, ModelBAdmin)
admin.site.register(ModelC, ModelCAdmin)
