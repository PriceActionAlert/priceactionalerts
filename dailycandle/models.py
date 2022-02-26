from django.db import models

# Create your models here.

class NTPC(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class UPL(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class SUNPHARMA(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class TATACONSUM(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class INDUSINDBK(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class ONGC(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class IOC(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class BHARTIARTL(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class ITC(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class WIPRO(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class TCS(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class BRITANNIA(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class COALINDIA(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"


class GRASIM(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)


    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class TATAMOTORS(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class TITAN(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class BPCL(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class JSWSTEEL(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class INFY(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class HDFC(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class DIVISLAB(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class SHREECEM(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class CIPLA(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class ADANIPORTS(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class HCLTECH(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class HINDALCO(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class BAJFINANCE(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class KOTAKBANK(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class ASIANPAINT(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class NESTLEIND(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class HDFCLIFE(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class ULTRACEMCO(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class RELIANCE(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class TATASTEEL(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class HINDUNILVR(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class SBILIFE(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class LT(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class DRREDDY(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class HDFCBANK(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class EICHERMOT(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class SBIN(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class BAJAJFINSV(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class AXISBANK(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class HEROMOTOCO(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class ICICIBANK(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class POWERGRID(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class TECHM(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class MARUTI(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"

class MM(models.Model):
    Finance = models.CharField(max_length=300, blank=True)
    Monday = models.CharField(max_length=1500, blank=True)
    Tuesday = models.CharField(max_length=1500, blank=True)
    Wednesday = models.CharField(max_length=1500, blank=True)
    Thursday = models.CharField(max_length=1500, blank=True)
    Friday = models.CharField(max_length=1500, blank=True)

    def __str__(self):
        return f" {self.id}: {self.Finance} {self.Monday} {self.Tuesday} {self.Wednesday} {self.Thursday} {self.Friday}"
