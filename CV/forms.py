from wtforms import Form, IntegerField, StringField, validators


class FormType(Form):
    choice = IntegerField('choice', [validators.NumberRange(min=1, max=4)])

    # def validate_choice(self, form, field):
    #     if field.data != range(1,4) :
    #         print("Je suis désolé je n'ai pas compris")


class FormName(Form):
    name = StringField(u'name', [validators.required(), validators.length(max=20)])

