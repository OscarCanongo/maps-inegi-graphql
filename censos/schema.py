import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Censo

class CensoType(DjangoObjectType):
    class Meta:
        model = Censo

class Query(graphene.ObjectType):
    censos = graphene.List(CensoType, idestado=graphene.String(), idmunicipio=graphene.String(), idactividad=graphene.String())

    def resolve_censos(self, info, idestado=None, idmunicipio=None, idactividad=None, **kwargs):
        if idestado and idmunicipio and not idactividad:
            filter = (
                Q(idestado=idestado) &
                Q(idmunicipio=idmunicipio)
            )
            return Censo.objects.filter(filter)

        if idestado and not idmunicipio and not idactividad:
            filter = (
                Q(idestado=idestado) 
            )
            return Censo.objects.filter(filter)

        if idestado and idactividad and not idmunicipio:
            filter = (
                Q(idestado=idestado) &
                Q(actividad__contains=idactividad)
            )
            return Censo.objects.filter(filter)

        return Censo.objects.all()


