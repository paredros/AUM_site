from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class HeroBanner(models.Model):
    mainText = RichTextField()
    showApplyNow = models.BooleanField()
    testImage = models.ImageField(upload_to='images/', null=True)
    logoImage1 = models.ImageField(upload_to='images/', null=True)

class ApplyBanner(models.Model):
    callToAction = models.CharField(max_length=255)
    landing1 = models.CharField(max_length=255)
    landing2 = models.CharField(max_length=255)
    explainTitle = models.CharField(max_length=255)
    explainText = models.TextField()
    applyLink = models.CharField(max_length=255, blank=True, default="")
    backImage = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "APPLY Banner Data"

class HeroGlobalData(models.Model):
    logoImage1 = models.ImageField(upload_to='images/', null=True)
    useClassicLogo = models.BooleanField(default=True)
    classicLogo = models.ImageField(upload_to='images/', null=True, blank=True)

class GlobalTextAndTitle(models.Model):
    blogTitleGeneral = models.CharField(max_length=255)

class BlogGeneral(models.Model):
    bannerTitle = models.CharField(max_length=255)
    bannerLine1 = models.CharField(max_length=255)
    bannerLine2 = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "BLOG General Data"

class ButtonsGeneral(models.Model):
    TalkToAdmission = models.CharField(max_length=255)
    TalkToAdmissionShort = models.CharField(max_length=50, default="Talk")
    TalkToAdmissionLink = models.CharField(max_length=255, blank=True, default="")
    GetLeaf = models.CharField(max_length=255)
    GetLeafShort = models.CharField(max_length=50, default="Get")
    Scholarship = models.CharField(max_length=255)
    ScholarshipShort = models.CharField(max_length=50, default="Get")
    BasicButton = models.CharField(max_length=50, default="View")

class ProgramsGeneral(models.Model):
    TextBig1 = models.CharField(max_length=255)
    PlanOutlineTitle = models.CharField(max_length=255, default="")
    FutureBanner = models.CharField(max_length=255, default="")
    FutureBanner_FirstLine = models.CharField(max_length=255, default="", blank=True)
    FutureBanner_SecondLine = models.CharField(max_length=255, default="")
    DegreeBanner = models.CharField(max_length=255, default="")
    DegreeBanner_FirstLine = models.CharField(max_length=255, default="", blank=True)
    DegreeBanner_SecondLine = models.CharField(max_length=255, default="", blank=True)


class ProgramData(models.Model):
    enabled = models.BooleanField(default=False)
    isGraduatedProgram = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    title = models.CharField(max_length=255, null=True, blank=True)
    backgroundColorMini = models.CharField(max_length=7, default="#CE1731")
    groupBachelor = models.CharField(max_length=255, null=True, blank=True)
    titleClarification = models.CharField(max_length=255, null=True, blank=True) #like *Pending NCFHE approval
    logoTxt = models.CharField(max_length=2, null=True, blank=True)
    shortTextTop = RichTextField(null=True, blank=True)
    shortTextMini = RichTextField(null=True, blank=True)
    bigImage = models.ImageField(upload_to='images/', null=True, blank=True)
    #more data
    yearsLong = models.IntegerField(default=5)
    tuitonFee = models.CharField(max_length=50, default="15,500*")
    tuitonFeeHasClarification = models.BooleanField(default=False)
    tuitonFeeClarification = models.TextField(default="", null=True, blank=True)
    description2 = RichTextField(default="",null=True, blank=True)
    creditsTotal = models.IntegerField(default=124)
    leafletHas = models.BooleanField(default=True)
    leafletUrl = models.URLField(null=True, blank=True)
    #data outline
    hasOutline = models.BooleanField(default=True)
    outlineXMLDATA = models.TextField(null=True, blank=True)
    futureBlock = models.TextField(default="",null=True, blank=True)
    futureBlock_keys = models.TextField(default="",null=True, blank=True)
    degreeBlock = models.TextField(default="",null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Programs Data"

class PageGeneral(models.Model):
    id_short_name = models.CharField(max_length=255)
    content = models.TextField()
    bigImage1 = models.ImageField(upload_to='images/', null=True, blank=True)
    bigImage2 = models.ImageField(upload_to='images/', null=True, blank=True)
    medImage1 = models.ImageField(upload_to='images/', null=True, blank=True)
    medImage2 = models.ImageField(upload_to='images/', null=True, blank=True)
    minImage1 = models.ImageField(upload_to='images/', null=True, blank=True)
    minImage2 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.id_short_name

    class Meta:
        verbose_name_plural = "Original Contentent Edition"

class Professor(models.Model):
    name = models.CharField(max_length=255)
    nameTitle = models.CharField(max_length=255)
    roleTitle = models.TextField(default="", blank=True)
    photoBig = models.ImageField(upload_to='images/people/', null=True, blank=True)
    photoMed = models.ImageField(upload_to='images/people/', null=True, blank=True)
    photoMin = models.ImageField(upload_to='images/people/', null=True, blank=True)
    photoTxt = models.CharField(max_length=3, default="", blank=True)
    nationality = models.CharField(max_length=255)
    social = models.TextField(default="", blank=True) #json
    about = models.TextField(default="", blank=True)
    currentPosition = models.TextField(default="", blank=True)
    #programs = models.TextField(default="", blank=True)
    skills = models.TextField(default="", blank=True)
    #education = models.TextField(default="", blank=True) #json
    #generalExperience = models.TextField(default="", blank=True) #json
    #educationalExperience = models.TextField(default="", blank=True) #json
    #scholarshipLinks = models.TextField(default="", blank=True)  # json
    #otherLinks = models.TextField(default="", blank=True)  # json
    bigRichData = RichTextField(default="", blank=True)

    def __str__(self):
        return self.name

class PageBasic(models.Model):
    id_short_name = models.CharField(max_length=255)
    bigImage1 = models.ImageField(upload_to='images/', null=True, blank=True)
    useVideoTop = models.BooleanField(default=True)
    useImageTop = models.BooleanField(default=False)
    tintOverlayTop = models.FloatField(default=0.7, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])
    useBackColorTop = models.BooleanField(default=False)
    colorBackTop = models.CharField(max_length=7, default="#E9EAE4")
    colorTextTop = models.CharField(max_length=7, default="#FFFFFF")
    invertNavColorTop = models.BooleanField(default=False)
    heroTitle = RichTextField(max_length=100)
    heroDescription = RichTextField(max_length=255)
    leftData = RichTextField(default="", blank=True)
    middleData = RichTextUploadingField(default="", blank=True,config_name='youtube', external_plugin_resources=[(
        'youtube',
        '/static/ckeditor_plugin/ckeditor_youtube/youtube/',
        'plugin.js'
    )])
    useRightData = models.BooleanField(default=False)
    rightData = RichTextField(default="", blank=True)
    useTopData = models.BooleanField(default=False)
    topData = RichTextUploadingField(default="", blank=True, config_name='youtube', external_plugin_resources=[(
        'youtube',
        '/static/ckeditor_plugin/ckeditor_youtube/youtube/',
        'plugin.js'
    )])
    useBottomData = models.BooleanField(default=False)
    bottomData = RichTextUploadingField(default="", blank=True, config_name='youtube', external_plugin_resources=[(
        'youtube',
        '/static/ckeditor_plugin/ckeditor_youtube/youtube/',
        'plugin.js'
    )])

    def __str__(self):
        return self.id_short_name

    class Meta:
        verbose_name_plural = "Generals Page Edition"

class NavSetting(models.Model):
    topNavBar = models.TextField(default="", blank=True)
    footerNav = models.TextField(default="", blank=True)

class ContactWebpage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name + " - " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name_plural = "Contact"


class NewsletterContact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email + " - " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name_plural = "Newsletter"