from django import forms

class PostForm(forms.Form):
	text = forms.CharField(required=True)
	imagem = forms.FileField() 

	def is_valid(self):
		valid = True
		if not super(PostForm, self).is_valid():
			self.adiciona_erro('Por favor verifique os dados informados')
			valid = False

		return valid

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)	 

