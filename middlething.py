#!/usr/bin/env python
# _*_coding:utf-8_*_
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Md1(MiddlewareMixin):

    def process_request(self, request):
        print("Md1请求")

    def process_response(self, request, response):
        print("Md1返回")
        return response

    def process_exception(self,callback_args, callback_kwargs):
        print('process1 error')
        return HttpResponse('error')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('Md1_views')



class Md2(MiddlewareMixin):

    def process_request(self, request):
        print("Md2请求")
        # return HttpResponse("Md2中断")

    def process_response(self, request, response):
        print("Md2返回")
        return response

    def process_exception(self,callback_args, callback_kwargs):
        print('process2 error')
        return HttpResponse('error')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('Md2_views')

