from django.shortcuts import render
from django.http import HttpResponse
import asyncio
from django.views import View

class AsyncPage(View):
    async def process1(self, request):
        data = []
        for i in range(1,100):
            data.append(i)
            await asyncio.sleep(0.00001)
        return data
    async def process2(self, request):
        data = []
        for i in range(100,200):
            data.append(i)
            await asyncio.sleep(0.00001)
        return data
    async def get(self, request):
        result = await asyncio.gather(
            self.process1(request),
            self.process2(request),
        )
        return HttpResponse(result)