from django import forms


class JsonModelForm(forms.ModelForm):

    def to_dict(self, *args, **kwargs):
        """ 
        convert all relevant data into a dictionary so it can be converted to 
        json and sent to js frontend. 'validator' & 'widget' have been removed
        as their information has been captured in the immediate dict

        self = {
            'instance': <Hobby: hockey>, 
            '_validate_unique': False, 
            'is_bound': False, 
            'data': <MultiValueDict: {}>, 
            'files': <MultiValueDict: {}>, 
            'auto_id': 'id_%s', 
            'initial': {
                'id': 4, 
                'name': 'hockey', 
                'comment': 'goal', 
                'available': True
            }, 
            'error_class': <class 'django.forms.utils.ErrorList'>, 
            'label_suffix': ':', 
            'empty_permitted': False, 
            '_errors': None, 
            'fields': {
                'name': <django.forms.fields.CharField object at 0x105682890>, 
                'comment': <django.forms.fields.CharField object at 0x105683d00>, 
                'available': <django.forms.fields.BooleanField object at 0x105682140>
            }, 
            '_bound_fields_cache': {}, 
            'renderer': <django.forms.renderers.DjangoTemplates object at 0x1056e90c0>
        }
        """
        form = {}
        fields = self.fields
        for field in fields:
            form[field] = fields[field].__dict__
            form[field]['input_type'] = self.get_input_type(form[field])
            del form[field]['validators']
            del form[field]['widget']
        if not self.initial:
            self.initial = self.get_initial_values(form)
        return {'initial': self.initial, 'fields': form}

    @staticmethod
    def get_input_type(field):
        """
        set the input type i.e. checkbox, text
        """
        # 'Textarea' does not have an input_type
        if isinstance(field['widget'], forms.widgets.Textarea):
            return 'text'
        return field['widget'].input_type

    @staticmethod
    def get_initial_values(form):
        """ 
        create an initial values dict for a new form with no instance which
        which is used as the initial form state in the form
        """
        initial = {}
        for field in form:
            if not field == 'id':
                initial[field] = form[field]['initial']
        return initial
