from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import duGioTable, KHDGTG_Table

def home(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render())

def duGio(request):
    mymembers = duGioTable.objects.all().values()
    template = loader.get_template('duGio.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  a = request.POST['hoTen']
  b = request.POST['toCM']
  c = request.POST['ngayDu']
  d = request.POST['phuChu']
  duGio = duGioTable(hoTen=a, toCM=b, ngayDu=c, phuChu=d)
  duGio.save()
  return HttpResponseRedirect(reverse('duGio'))

def update(request, id):
  mymember = duGioTable.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  hoTen = request.POST['hoTen']
  toCM = request.POST['toCM']
  ngayDu = request.POST['ngayDu']
  phuChu = request.POST['phuChu']
  member = duGioTable.objects.get(id=id)
  member.hoTen = hoTen
  member.toCM = toCM
  member.ngayDu = ngayDu
  member.phuChu = phuChu
  member.save()
  return HttpResponseRedirect(reverse('duGio'))

def delete(request, id):
  duGio = duGioTable.objects.get(id=id)
  duGio.delete()
  return HttpResponseRedirect(reverse('duGio'))

def sorting1(request):
  mydata = duGioTable.objects.filter(toCM='1').values()
 # mycount = duGioTable.objects.filter(toCM='1').values().count()
  template = loader.get_template('sorting.html')
  context = {
    'mymembers': mydata,
  }
 # print(mycount)
  return HttpResponse(template.render(context, request))

def sorting2(request):
  mydata = duGioTable.objects.filter(toCM='2').values()
  template = loader.get_template('sorting.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
def sorting3(request):
  mydata = duGioTable.objects.filter(toCM='3').values()
  template = loader.get_template('sorting.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
def sorting4(request):
  mydata = duGioTable.objects.filter(toCM='4').values()
  template = loader.get_template('sorting.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))

def KHDGTG(request):
    mymembers = KHDGTG_Table.objects.all().values()
    template = loader.get_template('khDG_TG.html')
    context = {
      'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def addKHDGTG(request):
  template = loader.get_template('addKHDGTG.html')
  return HttpResponse(template.render({}, request))

def addrecordKHDGTG(request):
  a = request.POST['hoTen']
  b = request.POST['toCM']
  c = request.POST['ngayDay']
  d = request.POST['tenBai']
  e = request.POST['lop']
  f = request.POST['luotDu']
  g = request.POST['loai']
  h = request.POST['xepLoai']
  i = request.POST['phuChu']
  KHDGTG = KHDGTG_Table(hoTen=a, toCM=b, ngayDay=c, tenBai=d,
                       lop=e, luotDu=f, loai=g, xepLoai=h, phuChu=i)
  KHDGTG.save()
  return HttpResponseRedirect(reverse('KHDGTG'))

def updateKHDGTG(request, id):
  mymember = KHDGTG_Table.objects.get(id=id)
  template = loader.get_template('updateKHDGTG.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecordKHDGTG(request, id):
  hoTen = request.POST['hoTen']
  toCM = request.POST['toCM']
  ngayDay = request.POST['ngayDay']
  tenBai = request.POST['tenBai']
  lop = request.POST['lop']
  luotDu = request.POST['luotDu']
  loai = request.POST['loai']
  xepLoai = request.POST['xepLoai']
  phuChu = request.POST['phuChu']

  member = KHDGTG_Table.objects.get(id=id)
  member.hoTen = hoTen
  member.toCM = toCM
  member.ngayDay = ngayDay
  member.tenBai = tenBai
  member.lop = lop
  member.luotDu = luotDu
  member.loai = loai
  member.xepLoai = xepLoai
  member.phuChu = phuChu
  member.save()
  return HttpResponseRedirect(reverse('KHDGTG'))

def deleteKHDGTG(request, id):
  duGio = KHDGTG_Table.objects.get(id=id)
  duGio.delete()
  return HttpResponseRedirect(reverse('KHDGTG'))