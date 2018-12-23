from servicebus import Servicebus


class AuthorisationRules(Servicebus):
    """AuthorisationRules generates arm template from input json"""
    access_policies_values = [
        ['Listen', 'Send'],
        ['Send', 'Listen'],
        ['Send'],
        ['Listen']
    ]

    def __init__(self, object):
        """
        Construct a new 'AuthorisationRules' objectself.

        :param object: The object needs access policies 'Topic' or 'Queue'
        """

        self.object_type = object.object_type
        self.object_name = object.object_name
        self.template_path = 'templates/authorisationRule.json.template'
        self.data = object.data
        try:
            self.access_policies = self.data['accessPolicies']
        except KeyError:
            print('Obj {} has no acces policy rule.'.format(self.object_name))
            self.access_policies = []

    def get_policy_name(self, access_policy_type):
        """
        Generate full acces policy name

        :param: access_policy_type: Type of access policy like a ['Send']
        :return: Access policy full name without dash
        """
        def convertArrayTostring(ap_list):
            str = ''
            if len(ap_list) == 2:
                str = '{}{}'.format(ap_list[0], ap_list[1])
            else:
                str = ap_list[0]

            return str

        import re

        def callback(pat): return pat.group(1).upper()
        return re.sub(r'-([a-z]){1}', callback, self.object_name) \
            + convertArrayTostring(access_policy_type) \
            + 'Policy'

    def get_default(self, access_policy_type):
        """
        Returns default azure AM arm parameters.

        :param: access_policy_type: Type of access policy like a ["Send"]
        :return: Azure arm default parameters Dictionary
        """
        import json

        assert access_policy_type in self.access_policies_values, \
            'Access policy value {} is not allowed.'.format(access_policy_type)

        return {
            'objectName': self.object_name,
            'objectType': self.object_type,
            'policy_name': self.get_policy_name(access_policy_type),
            # Convert ['Send'] to ["Send"]
            'auth_rules_list': json.dumps(access_policy_type, indent=None)
        }

    def __repr__(self):
        from jinja2 import Template

        with open(self.template_path) as f:
            template = Template(f.read())

        ap_all = ''
        for ap in self.access_policies:
            attr = self.get_default(access_policy_type=ap)
            ap_all += template.render(attr)
        return ap_all


if __name__ == '__main__':
    import json
    import topic

    with open('./definition/topics/testTopic.json') as f:
        data = json.load(f)

    t = topic.Topic(json_definition=data)
    a = AuthorisationRules(t)
    print(a)
