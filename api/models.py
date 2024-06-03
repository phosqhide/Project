from tastypie.resources import ModelResource
from shop.models import Category, Course
from .aunthentication import CustomAuthentication
from tastypie.authorization import Authorization
# Create your models here.


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methodts = ['get', 'post', 'delete']
        excludes = ['reviews_qty', 'created_add']
        aunthetication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category'] = bundle.obj.category
        bundle.data['category_id'] = bundle.obj.category_id
        return bundle

    def dehydrate_title(self, bundle):
        return bundle.data['title'].upper()
