from django.db import models
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class Pet(models.Model):
    dog = "Dog"
    cat = "Cat"
    male = "Male"
    female = "Female"
    rab = "rabies"
    bor = "Bordtella"
    can = "Canine Distemper / Parvo Combo"
    inf = "Canine Influenza"
    lep4 = "Leptospirosis (Lepto4)"
    c3 = "Canine C3"
    c4 = "Canine C4"
    c5 = "Canine C5"
    c7 = "Canine C7"
    fvrcp = "Feline FVRCP group (rhino, calic, distemper)"
    fhv = "Feline Herpesvirus (FHV)"
    fcv = "Feline Calicivirus (FCV)"
    fpk = "Feline Panleukopenia (FPK)"
    TYPE_CHOICES = [(dog,"Dog"),(cat, "Cat")]
    GENDER_CHOICES = [(male, "Male"),(female, "Female")]
    VACCINATION_CHOICES = [
        (rab,'Rabies'),(bor,'Bordtella'),(can,'Canine Distemper / Parvo Combo'),(inf,'Canine Influenza'),
        (lep4,'Leptospirosis (Lepto4)'),(c3,'Canine C3'),(c4,'Canine C4'),(c5,'Canine C5'),(c7,'Canine C7'),
        (fvrcp,'Feline FVRCP group (rhino, calic, distemper)'),(fhv,'Feline Herpesvirus (FHV)'),
        (fcv,'Feline Calicivirus (FCV)'),(fpk,'Feline Panleukopenia (FPK)')]
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    name = models.CharField(max_length=30, null=False)
    pet_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    breed = models.CharField(max_length=30, blank=False, null=False)
    gender = models.CharField(max_length=10, null=False, default=None, choices=GENDER_CHOICES)
    son = models.BooleanField(verbose_name='sprayed / neutered', default=False)
    weight = models.IntegerField(null=True, blank=True)
    coat = models.CharField(max_length=20)
    birthday = models.DateField(null=True, blank=True)
    allergies_notes = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    vaccine = models.CharField(max_length=40, choices=VACCINATION_CHOICES, blank=True)
    allergies = models.BooleanField(blank=True,)
    anal_gland = models.BooleanField(verbose_name='Anal Gland Issues')
    arthirits = models.BooleanField(verbose_name='Arthritis')
    blind = models.BooleanField(verbose_name='Blind / Poor Vision')
    trachea = models.BooleanField(verbose_name='Collapsing Trachea')
    deaf = models.BooleanField(verbose_name='Deaf/Poor vision')
    diabetic = models.BooleanField(verbose_name='Diabetic')
    standing = models.BooleanField(verbose_name='Difficulty Standing')
    epileptic = models.BooleanField(verbose_name='Epileptic')
    heart = models.BooleanField(verbose_name='Heart Problems')
    hip = models.BooleanField(verbose_name='Hip Dysplasia')
    hot = models.BooleanField(verbose_name='Hot Spots')
    incontinence = models.BooleanField(verbose_name='Incontinence')
    kidney = models.BooleanField(verbose_name='Kidney Disease')
    moles = models.BooleanField(verbose_name='Moles & Warts')
    pancreatitis = models.BooleanField(verbose_name='Pancreatitis')
    ear = models.BooleanField(verbose_name='Prone to ear infection')
    skin = models.BooleanField(verbose_name='Sensitive Skin')
    tooth = models.BooleanField(verbose_name='Tooth Decay')
    tumors = models.BooleanField(verbose_name='Tumors / Cysts')
    anxiety = models.BooleanField(verbose_name='Anxiety')
    cage = models.BooleanField(verbose_name='Cage Aggressive')
    clippers = models.BooleanField(verbose_name='Fear of Clippers')
    dryer = models.BooleanField(verbose_name='Fear of Dryer')
    nail = models.BooleanField(verbose_name='Fear of nail clipping')
    water = models.BooleanField(verbose_name='Fear of warter')
    shedding = models.BooleanField(verbose_name='Heavy Shedding')
    hernia = models.BooleanField(verbose_name='Hernia')
    energy = models.BooleanField(verbose_name='High energy')
    biting = models.BooleanField(verbose_name='History of biting')
    leash = models.BooleanField(verbose_name='Leash required')
    soiler = models.BooleanField(verbose_name='Nervous soiler')
    prefumes = models.BooleanField(verbose_name='Np Perfumes')
    photo = models.BooleanField(verbose_name='No public photos')
    animal = models.BooleanField(verbose_name='Potential Aggression w/ animals')
    people = models.BooleanField(verbose_name='Potential Aggression w/ people')
    clipper_burn = models.BooleanField(verbose_name='Prone to clipper burn')
    senior = models.BooleanField(verbose_name='senior pet')
    table = models.BooleanField(verbose_name='Table/Kennel diver')
    team = models.BooleanField(verbose_name='Team lift')
    chew = models.BooleanField(verbose_name='Tends to chew')
    timid = models.BooleanField(verbose_name='Timid/Shy')
    barker = models.BooleanField(verbose_name='Vocal/Barker')

    class Meta:
        verbose_name_plural = 'Pets'
