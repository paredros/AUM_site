from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from aum.models import *
from django.utils import timezone
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from aum.forms import NewsletterForm
import json

# Create your views here.
def viewallblogs(request):
    dt = datetime.datetime.now().timestamp()
    passget = "?"
    authorfind = request.GET.get('author')
    tagfind = request.GET.get('tag')
    if authorfind:
        posts = get_list_or_404(Post, enabled=True, author=authorfind)
        passget="author="+authorfind+"&"
    elif tagfind:
        posts = get_list_or_404(Post, enabled=True, tags__name__in=[tagfind])
        passget = "tag=" + tagfind + "&"
    else:
        posts = get_list_or_404(Post, enabled=True)
    page = request.GET.get('page')

    paginator = Paginator(posts, 2)
    posts_page = paginator.get_page(page)

    topdata = HeroGlobalData.objects.first()
    settingstop = {
        'minilogotxt': "BLO",
        'usevideo': True,
        'useimg': False,
        'imgurl': None,
        'tintoverlay': 0.5,
        'usebackcolor': False,
        'colorback': '#121212',
        'typemodel': 'program',
        'texttop': "AUM Live",
        'textbody': "bbkakkabak"
    }

    formnewsletter = ""
    msgs_alert = {}

    if request.method == 'POST':
        formnewsletter = NewsletterForm(request.POST)
        if formnewsletter.is_valid():
            msgs_alert["Newsletter"] = True
            formnewsletter.save()
            formnewsletter = NewsletterForm()

    else:
        formnewsletter = NewsletterForm()

    navdata = NavSetting.objects.first()
    topnav = json.loads(navdata.topNavBar)
    footernav = json.loads(navdata.footerNav)
    floatnav = json.loads(navdata.floatNav)
    applybanner = ApplyBanner.objects.first()
    settingsapply = {
        'call': applybanner.callToAction,
        'landing1': applybanner.landing1,
        'landing2': applybanner.landing2,
        'applyLink': applybanner.applyLink,
        'tipo': 'circulo'
    }
    generaldata = GlobalTextAndTitle.objects.first()

    return render(request,'blog/listall.html', {'posts':posts_page,
                                                'timestamp':dt,
                                                'passget':passget,
                                                'settingstop': settingstop,
                                                'topdata':topdata,
                                                'settingsapply': settingsapply,
                                                'generaldata': generaldata,

                                                })

def post(request, id_slug):
    dt = datetime.datetime.now().timestamp()
    post = get_object_or_404(Post, slug=id_slug)

    return render(request, 'blog/viewpost.html', {'post': post, 'timestamp': dt})

def viewallforce(request):
    dt = datetime.datetime.now().timestamp()
    posts = get_list_or_404(Post, enabled=True)
    return render(request, 'blog/listallforce.html', {'posts': posts, 'timestamp': dt})


def bloggeneral(request):
    dt = datetime.datetime.now().timestamp()

    passget = "?"
    authorfind = request.GET.get('author')
    tagfind = request.GET.get('tag')
    if authorfind:
        posts = get_list_or_404(Post, enabled=True, author=authorfind)
        passget = "?author=" + authorfind + "&"
    elif tagfind:
        posts = get_list_or_404(Post, enabled=True, tags__name__in=[tagfind])
        passget = "?tag=" + tagfind + "&"
    else:
        posts = get_list_or_404(Post, enabled=True)
    page = request.GET.get('page')

    paginator = Paginator(posts, 2)
    posts_page = paginator.get_page(page)

    navdata = NavSetting.objects.first()
    topnav = json.loads(navdata.topNavBar)
    footernav = json.loads(navdata.footerNav)
    floatnav = json.loads(navdata.floatNav)
    generaldata = GlobalTextAndTitle.objects.first()
    topdata = HeroGlobalData.objects.first()
    applybanner = ApplyBanner.objects.first()
    buttonsgeneral = ButtonsGeneral.objects.first()
    bloggeneral = BlogGeneral.objects.first()

    formnewsletter = ""
    msgs_alert = {}

    if request.method == 'POST':
        formnewsletter = NewsletterForm(request.POST)
        if formnewsletter.is_valid():
            msgs_alert["Newsletter"] = True
            formnewsletter.save()
            formnewsletter = NewsletterForm()

    else:
        formnewsletter = NewsletterForm()

    settingsapply = {
        'call': applybanner.callToAction,
        'landing1': applybanner.landing1,
        'landing2': applybanner.landing2,
        'applyLink': applybanner.applyLink,
        'tipo': 'circulo'
    }
    topimg = ''

    settingstop = {
        'minilogotxt': "BLO",
        'invertnavcolor':False,
        'usevideo': True,
        'useimg': False,
        'imgurl': None,
        'tintoverlay': 0.5,
        'usebackcolor': False,
        'colorback': '#121212',
        'typemodel': 'generalpage',
        'texttop': "<strong>AUM</strong> Live",
        'textbody': "A Place To Share Experiences"
    }

    return render(request,'blog/listall.html', {'settingstop': settingstop,
                                                'posts': posts_page,
                                                'passget': passget,
                                                    "timestamp": dt,
                                                    'topdata':topdata,
                                                    'settingsapply': settingsapply,
                                                    'buttonsgeneral': buttonsgeneral,
                                                    'bloggeneral':bloggeneral,
                                                    'generaldata':generaldata,
                                                    'topnav':topnav,
                                                    'footernav': footernav,
                                                    'floatnav':floatnav,
                                                    'msgs_alert': msgs_alert,
                                                    'formnewsletter': formnewsletter,
                                                    'viewintroanim': False
                                                 })

def postenhanced(request, id_slug):
    dt = datetime.datetime.now().timestamp()

    post = get_object_or_404(Post, slug=id_slug)

    navdata = NavSetting.objects.first()
    topnav = json.loads(navdata.topNavBar)
    footernav = json.loads(navdata.footerNav)
    floatnav = json.loads(navdata.floatNav)
    generaldata = GlobalTextAndTitle.objects.first()
    topdata = HeroGlobalData.objects.first()
    applybanner = ApplyBanner.objects.first()
    buttonsgeneral = ButtonsGeneral.objects.first()
    bloggeneral = BlogGeneral.objects.first()

    formnewsletter = ""
    msgs_alert = {}

    if request.method == 'POST':
        formnewsletter = NewsletterForm(request.POST)
        if formnewsletter.is_valid():
            msgs_alert["Newsletter"] = True
            formnewsletter.save()
            formnewsletter = NewsletterForm()

    else:
        formnewsletter = NewsletterForm()

    settingsapply = {
        'call': applybanner.callToAction,
        'landing1': applybanner.landing1,
        'landing2': applybanner.landing2,
        'applyLink': applybanner.applyLink,
        'tipo': 'circulo'
    }
    topimg = ''

    settingstop = {
        'minilogotxt': "BLO",
        'invertnavcolor':False,
        'usevideo': False,
        'useimg': True,
        'imgurl': post.bigPicture,
        'tintoverlay': 0.7,
        'usebackcolor': False,
        'colorback': '#121212',
        'typemodel': 'blogholder',
        'texttop': post.title,
        'textbody': post.summary
    }
    return render(request,'blog/viewpost.html', {'settingstop': settingstop,
                                                'post': post,
                                                    "timestamp": dt,
                                                    'topdata':topdata,
                                                    'settingsapply': settingsapply,
                                                    'buttonsgeneral': buttonsgeneral,
                                                    'bloggeneral':bloggeneral,
                                                    'generaldata':generaldata,
                                                    'topnav':topnav,
                                                    'footernav': footernav,
                                                    'floatnav':floatnav,
                                                    'msgs_alert': msgs_alert,
                                                    'formnewsletter': formnewsletter,
                                                    'viewintroanim': False
                                                 })