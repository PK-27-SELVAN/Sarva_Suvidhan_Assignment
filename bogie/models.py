from django.db import models

class BMBCChecksheet(models.Model):
    adjustingTube = models.CharField(max_length=100)
    cylinderBody = models.CharField(max_length=100)
    pistonTrunnion = models.CharField(max_length=100)
    plungerSpring = models.CharField(max_length=100)

class BogieChecksheet(models.Model):
    axleGuide = models.CharField(max_length=100)
    bogieFrameCondition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolsterSuspensionBracket = models.CharField(max_length=100)
    lowerSpringSeat = models.CharField(max_length=100)

class BogieDetails(models.Model):
    bogieNo = models.CharField(max_length=100)
    dateOfIOH = models.DateField()
    deficitComponents = models.CharField(max_length=100)
    incomingDivAndDate = models.CharField(max_length=100)
    makerYearBuilt = models.CharField(max_length=100)

class BogieInspection(models.Model):
    formNumber = models.CharField(max_length=100, unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bmbcChecksheet = models.OneToOneField(BMBCChecksheet, on_delete=models.CASCADE)
    bogieChecksheet = models.OneToOneField(BogieChecksheet, on_delete=models.CASCADE)
    bogieDetails = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)

