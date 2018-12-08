from django.shortcuts import render, get_object_or_404
from .models import *
import json
import datetime
from .forms import ContactForm, NewsletterForm

# Create your views here.
def home(request):
    herodata = HeroBanner.objects.first()
    programs = ProgramData.objects.filter(enabled=True, isGraduatedProgram=False).order_by('order').only('pk',
                                                                                                         'title',
                                                                                                         'backgroundColorMini',
                                                                                                         'groupBachelor',
                                                                                                         'logoTxt',
                                                                                                         'shortTextMini',
                                                                                                         'bigImage')
    dt = datetime.datetime.now().timestamp()
    return render(request,'aum/home.html', {'herodata':herodata,
                                            "timestamp":dt,
                                            "listPrograms":programs
                                            })

def paramhome(request):
    return pages(request,'home')

def program(request, program_id):
    data = get_object_or_404(ProgramData, pk=program_id)
    topdata = HeroGlobalData.objects.first()
    imgtop = ""
    if data.bigImage:
        imgtop = data.bigImage

    settingstop = {
        'minilogotxt':data.logoTxt,
        'usevideo':True,
        'useimg':False,
        'imgurl':imgtop,
        'tintoverlay':0.9,
        'usebackcolor':False,
        'colorback':'#121212',
        'typemodel':'program',
        'texttop':data.title,
        'textbody':data.shortTextTop
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
    applybanner = ApplyBanner.objects.first()
    settingsapply = {
        'call':applybanner.callToAction,
        'landing1':applybanner.landing1,
        'landing2': applybanner.landing2,
        'applyLink': applybanner.applyLink,
        'tipo':'circulo'
    }
    generaldata = GlobalTextAndTitle.objects.first()
    bloggeneral = BlogGeneral.objects.first()
    proggeneral = ProgramsGeneral.objects.first()
    buttonsgeneral = ButtonsGeneral.objects.first()

    dt = datetime.datetime.now().timestamp()

    tabla = json.loads(data.outlineXMLDATA)
    future = json.loads(data.futureBlock)
    future_key = json.loads(data.futureBlock_keys)
    degree = json.loads(data.degreeBlock)
    return render(request, 'aum/program_temp.html', {'data':data,
                                                     'topdata':topdata,
                                                     'settingstop':settingstop,
                                                     "timestamp":dt,
                                                     'settingsapply':settingsapply,
                                                     'generaldata':generaldata,
                                                     'bloggeneral':bloggeneral,
                                                     'proggeneral':proggeneral,
                                                     'buttonsgeneral':buttonsgeneral,
                                                     'tabla':tabla,
                                                     'future':future,
                                                     'future_key':future_key,
                                                     'degree':degree,
                                                     'topnav':topnav,
                                                     'footernav':footernav,
                                                     'msgs_alert': msgs_alert,
                                                     'formnewsletter': formnewsletter,
                                                     'viewintroanim': False
                                                     })


def pages(request, page_id):
    dt = datetime.datetime.now().timestamp()
    data = get_object_or_404(PageGeneral, id_short_name=page_id)
    content = json.loads(data.content)
    settingstop = content["settingstop"]
    form = ""
    formnewsletter=""
    msgs_alert = {}

    if request.method == 'POST':
        if "message" in request.POST: #is contact
            if page_id == "contactus":
                form = ContactForm(request.POST)
                if form.is_valid():
                    msgs_alert["FormContact"]=True
                    form.save()
                    form = ContactForm()
                    pass
        else: #is newsletter
            formnewsletter = NewsletterForm(request.POST)
            if formnewsletter.is_valid():
                msgs_alert["Newsletter"] = True
                formnewsletter.save()
                formnewsletter = NewsletterForm()
    else:
        formnewsletter = NewsletterForm()
        if page_id == "contactus":
            form = ContactForm()


    isHome = False;
    if page_id=='home':
        isHome = True

    navdata = NavSetting.objects.first()
    topnav = json.loads(navdata.topNavBar)
    footernav = json.loads(navdata.footerNav)
    generaldata = GlobalTextAndTitle.objects.first()
    topdata = HeroGlobalData.objects.first()
    applybanner = ApplyBanner.objects.first()
    buttonsgeneral = ButtonsGeneral.objects.first()
    bloggeneral = BlogGeneral.objects.first()
    settingsapply = {
        'call': applybanner.callToAction,
        'landing1': applybanner.landing1,
        'landing2': applybanner.landing2,
        'applyLink': applybanner.applyLink,
        'explainTitle':applybanner.explainTitle,
        'explainText': applybanner.explainText,
        'tipo': 'circulo'
    }
    if 'userectbanner' in settingstop.keys():
        if settingstop["userectbanner"]:
            if settingstop["typebanner"] == "talk":
                settingsapply["tipo"]="talk"
            if settingstop["typebanner"] == "talkcirculo":
                settingsapply["tipo"] = "talkcirculo"
            if settingstop["typebanner"] == "apply":
                settingsapply["tipo"] = "largo"
                settingsapply["explainTitle"] = settingstop["textbanner"]
                settingsapply["explainText"] = settingstop["textbanner_detail"]
            if settingstop["typebanner"] == "hide":
                settingsapply["tipo"] = "hide"
            if settingstop["typebanner"] == "largo":
                settingsapply["tipo"] = "largo"
                settingsapply["backImage"] = applybanner.backImage

    if 'variantbanner' in settingstop.keys():
        settingsapply["variantbanner"] = settingstop["variantbanner"]
    else:
        settingsapply["variantbanner"] = None;

    otherdata={}
    if 'useextradata' in settingstop.keys():
        if settingstop["useextradata"] == "professors":
            profData = Professor.objects.only('pk','nameTitle','roleTitle','photoMed','photoTxt')
            otherdata["professors"] = profData
        if settingstop["useextradata"] == "programs":
            progData = ProgramData.objects.filter(enabled=True, isGraduatedProgram=False).order_by('order').only('pk',
                                                                                                                 'title',
                                                                                                                 'backgroundColorMini',
                                                                                                                 'groupBachelor',
                                                                                                                 'logoTxt',
                                                                                                                 'shortTextMini',
                                                                                                                 'bigImage')
            otherdata["programs"] = progData
    return render(request,'aum/page_temp.html', {'settingstop': settingstop,
                                                    "timestamp": dt,
                                                    'topdata':topdata,
                                                    'settingsapply': settingsapply,
                                                    'buttonsgeneral': buttonsgeneral,
                                                    'content':content,
                                                    'bloggeneral':bloggeneral,
                                                    'generaldata':generaldata,
                                                    'data_bigImage1':data.bigImage1,
                                                    'data_bigImage2':data.bigImage2,
                                                    'data_medImage1':data.medImage1,
                                                    'data_medImage2':data.medImage2,
                                                    'data_minImage1':data.minImage1,
                                                    'data_minImage2':data.minImage2,
                                                    'otherdata':otherdata,
                                                    'topnav':topnav,
                                                 'footernav': footernav,
                                                 'form':form,
                                                 'msgs_alert':msgs_alert,
                                                 'formnewsletter':formnewsletter,
                                                 'viewintroanim':False,
                                                 'isHome':isHome
                                                 })

def professors(request, prof_id):
    dt = datetime.datetime.now().timestamp()
    data = get_object_or_404(Professor, pk=prof_id)
    navdata = NavSetting.objects.first()
    topnav = json.loads(navdata.topNavBar)
    footernav = json.loads(navdata.footerNav)
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
        'tipo': 'data'
    }
    settingstop = {
        'invertnavcolor':True,
        'minilogotxt': data.photoTxt,
        'usevideo': False,
        'useimg': False,
        'imgurl': "",
        'tintoverlay': 0,
        'usebackcolor': True,
        'colorback': '#E9EAE4',
        'typemodel': 'professor',
        'texttop': data.nameTitle,
        'textbody': data.roleTitle
    }

    sectionMain={
        "column1": [
            {
                "blocktype": "title",
                "value": data.nameTitle
            },
            {
                "blocktype": "Space",
                "value": 20
            },
            {
                "blocktype": "NormalMiniText",
                "value": data.nationality
            },
            {
                "blocktype": "Space",
                "value": 20
            },
            {
                "blocktype": "socialbar",
                "value": json.loads(data.social)
            }
        ],
        "column2": [
            {
                "blocktype": "MoreBigText",
                "value": "<strong>About</strong>"
            },
            {
                "blocktype": "Space",
                "value": 25
            },
            {
                "blocktype": "MediumText",
                "value": data.about
            },
            {
                "blocktype": "Space",
                "value": 100
            }
        ]
    }
    sectionCurrentPos = {
        "column1": [
            {
                "blocktype": "title",
                "rightalign":True,
                "value": "Current Position"
            }
        ],
        "column2": [
            {
                "blocktype": "BigText",
                "value": data.currentPosition
            },
            {
                "blocktype": "Space",
                "value": 50
            }
        ]
    }
    skillsanddata = {
        "column1": [
            {
                "blocktype": "title",
                "rightalign": True,
                "value": "Skills"
            }
        ],
        "column2": [
            {
                "blocktype": "MediumText",
                "value": data.skills
            },
            {
                "blocktype": "Space",
                "value": 50
            },
            {
                "blocktype": "RichText",
                "value": data.bigRichData
            }
        ]
    }
    return render(request, 'aum/professor_temp.html', {'settingstop': settingstop,
                                                        "timestamp": dt,
                                                        'topdata': topdata,
                                                        'settingsapply': settingsapply,
                                                        'buttonsgeneral': buttonsgeneral,
                                                        'bloggeneral': bloggeneral,
                                                        'generaldata': generaldata,
                                                        'data_medImage1': data.photoMed,
                                                        'sectionMain':sectionMain,
                                                        'sectionCurrentPos':sectionCurrentPos,
                                                        'skillsanddata':skillsanddata,
                                                        'topnav':topnav,
                                                       'footernav': footernav,
                                                       'msgs_alert': msgs_alert,
                                                       'formnewsletter': formnewsletter,
                                                       'viewintroanim': False
                                                    })

def generalpages(request, page_id):
    dt = datetime.datetime.now().timestamp()
    data = get_object_or_404(PageBasic, id_short_name=page_id)

    navdata = NavSetting.objects.first()
    topnav = json.loads(navdata.topNavBar)
    footernav = json.loads(navdata.footerNav)
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
    if data.bigImage1:
        topimg = data.bigImage1.url

    settingstop = {
        'invertnavcolor': data.invertNavColorTop,
        'usevideo': data.useVideoTop,
        'useimg': data.useImageTop,
        'imgurl': topimg,
        'tintoverlay': data.tintOverlayTop,
        'usebackcolor': data.useBackColorTop,
        'colorback': data.colorBackTop,
        'colortext': data.colorTextTop,
        'typemodel': 'generalpage',
        'texttop': data.heroTitle,
        'textbody':data.heroDescription
    }

    return render(request,'aum/general_temp.html', {'settingstop': settingstop,
                                                    "timestamp": dt,
                                                    'topdata':topdata,
                                                    'settingsapply': settingsapply,
                                                    'buttonsgeneral': buttonsgeneral,
                                                    'bloggeneral':bloggeneral,
                                                    'generaldata':generaldata,
                                                    'data_bigImage1':data.bigImage1,
                                                    'data':data,
                                                    'topnav':topnav,
                                                    'footernav': footernav,
                                                    'msgs_alert': msgs_alert,
                                                    'formnewsletter': formnewsletter,
                                                    'viewintroanim': False
                                                 })