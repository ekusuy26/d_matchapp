from django.shortcuts import render, redirect
from accounts.models import Dog
from django.core.paginator import Paginator
from . import forms
from .models import Image
from PIL import Image
import cv2
from django.conf import settings

# Create your views here.

def topPage(request):
    if request.user.is_authenticated:
        return redirect('myhp:index')
    else:
        return render(request, 'myhp/topPage.html', {})

def index(request):
    headLine = 'ユーザー一覧'
    all_objs = Dog.objects.order_by('-id')
    paginator = Paginator(all_objs, 12) # 1ページに12件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    objs = paginator.get_page(p) # 指定のページのDogを取得
    dog = Dog.objects.filter(user_id=request.user.id)
    if dog.count() == 0:
        dog_flg = 0
    else:
        dog_flg = 1
    return render(request, 'myhp/index.html', {
        'headLine': headLine,
        'objs': objs,
        'dog_flg': dog_flg,
    })

def fusion(request, pk):
    opponent = Dog.objects.get(id = pk)
    headLine = '合成してみる'
    return render(request, 'myhp/fusion.html', {
        'opponent': opponent,
        'headLine': headLine,
    })

def result(request, pk):
    headLine = '結果'
    myself = Dog.objects.get(user_id = request.user.id)
    opponent = Dog.objects.get(id = pk)
    input_path = settings.BASE_DIR + myself.image.url
    input_path_two = settings.BASE_DIR + opponent.image.url
    output_path = settings.BASE_DIR + "/media/results/output" + str(request.user.id) + str(pk) + ".jpg"
    output_path_two = settings.BASE_DIR + "/media/results/output_two" + str(request.user.id) + str(pk) + ".jpg"
    src = cv2.imread(input_path)
    src_two = cv2.imread(input_path_two)
    img = src.copy()
    img_two = src_two.copy()
    def face_swap(src, src_two, x, y, width, height, ratio=1):
        dst = src.copy()
        dst_02 = src_two.copy()
        dst[y:y + height, x:x + width] = dst_02[y:y + height, x:x + width]
        return dst
    face_cascade_path = './haarcascade_frontalcatface.xml'
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    face_cascade_two = cv2.CascadeClassifier(face_cascade_path)
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    src_two_gray = cv2.cvtColor(src_two, cv2.COLOR_BGR2GRAY)
    img_two_gray = cv2.cvtColor(img_two, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(src_gray)
    faces_two = face_cascade_two.detectMultiScale(img_two_gray)
    for x, y, w, h in faces:
        for a, b, c, d in faces_two:
            dst_face_01 = face_swap(src, src_two, x, y, w, h)
            dst_face_02 = face_swap(img_two, img, a, b, c, d)
    
            cv2.imwrite(output_path, dst_face_01)
            cv2.imwrite(output_path_two, dst_face_02)
    img_tbl = Image()
    img_tbl.first_image = output_path
    img_tbl.second_image = output_path_two
    img_tbl.save()
    new_image = Image.objects.latest('id')
    new_image.users.add(request.user)
    new_image.users.add(opponent.user.id)

    return render(request, 'myhp/result.html', {
        'opponent': opponent,
        'headLine': headLine,
    })
