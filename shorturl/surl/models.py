from django.db import models
from django.core.urlresolvers import reverse
import re

#@jake:4/13/2016 class for storing values from wordlist and indicators showing whether these words are used
class relate(models.Model):
		words=models.CharField(max_length=200)
		usedflag=models.CharField(max_length=2,default='N')
#@jake:4/13/2016 class for storing actual url fields and an indicatore for their corresponding keywords
class Link(models.Model):
	url=models.URLField()
	word_ind=models.IntegerField(null=True)
#@jake:4/13/2016 This method does all the mapping and checks for assigning a new keyword
	@staticmethod
	def shorten(link):
		l2=Link.objects.get(url=link.url)
		if l2.pk==None:
			l2.url=link.url.lower()
			l2.save()

#@jake:4/13/2016 checks if the word is not allocated already for a url
		if l2.word_ind==None:
#@jake:4/13/2016 Parsing the html
			s=re.sub('[^0-9a-zA-Z]+',' ',link.url).lower().split(' ')
			for i in ['http','https','com','www']:
				if i in s:
					s.remove(i)
#@jake:4/13/2016 Reversing the list of words in html since the words are read from beginging to end by the parser
#@jake:4/13/2016 Check each words in the html for a match in word list which is unused
			s.reverse()
			for stn in s:
				l3=relate.objects.filter(words=stn,usedflag='N')
#				l2.word_ind=6
#				l2.save()
				if len(l3)!=0:
					l2.word_ind=l3[0].pk
					l3[0].usedflag='Y'
#					defret=l3[0].words
					l2.save()
					l3[0].save()
					break
#@jake:4/13/2016 if a match is not found, picks an unused word list
		if l2.word_ind == None:
			l3=relate.objects.filter(usedflag='N')
			if len(l3)!=0:
				l2.word_ind=l3[0].pk
				l2.save()
				l3[0].usedflag='Y'
				l3[0].save()
				defret=l3[0].words
#@jake:4/13/2016 if all the words are used up delete the oldest entry of html and use its keyword for the new url			
			else:
				l4=Link.objects.order_by('id')
				if len(l4)!=0:
					l3=relate.objects.get(pk=l4[0].word_ind)
					storevar=l3.pk
					l4[0].delete()	
					l2.word_ind=storevar
					l2.save()

		return l2.pk 	 				
#@jake:4/13/2016 This method is used for returning the right url for a short url
	@staticmethod
	def expand(slug):
		 l=slug
		 l3=relate.objects.get(words=l)
		 l2=Link.objects.get(word_ind=l3.pk)
		 return l2.url	
#@jake:4/13/2016 for getting the absolute url
	def get_absolute_url(self): 
		return reverse("link_show", kwargs={"pk": self.pk}) 
#@jake:4/13/2016 for displaying short url 
	def short_url(self):
		Link.shorten(self)
		l2=Link.objects.get(url=self.url)
		l3=relate.objects.get(pk=l2.word_ind)
		return reverse("redirect_short_url",kwargs={"short_url":l3.words})
	
	


#    def short_url(self):
 #   	return reverse("redirect_short_url",kwargs={"short_url": Link.shorten(self)}) 



         