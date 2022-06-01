import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Company
# Create your views here.


class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id == 0):
            companies = list(Company.objects.values())
            data = {'companies': companies}
        else:
            companies = list(Company.objects.filter(id=id).values())
            company = companies[0] if len(companies) > 0 else None
            data = {'company': company}

        return JsonResponse(data)

    def post(self, request):
        body = json.loads(request.body)
        company = Company.objects.create(
            name=body['name'],
            website=body['website'],
            foundation=body['foundation']
        )
        company = model_to_dict(company)
        data = {'company': company}
        return JsonResponse(data)

    def put(self, request, id):
        body = json.loads(request.body)
        companies = Company.objects.filter(id=id).all()
        if len(companies) <= 0:
            return JsonResponse({'message': 'Company not found'})

        company = Company.objects.get(id=id)
        company.name = body['name']
        company.website = body['website']
        company.foundation = body['foundation']
        company.save()

        company = model_to_dict(company)
        return JsonResponse({'company': company})

    def delete(self, request, id):
        companies = Company.objects.filter(id=id).all()
        if len(companies) <= 0:
            return JsonResponse({'message': 'Company not found'})

        company = Company.objects.get(id=id)
        company.delete()

        company = model_to_dict(company)
        return JsonResponse({'company': company})
