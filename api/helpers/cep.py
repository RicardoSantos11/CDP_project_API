import re


class Cep:

    def __init__(self):
        """
        'CLASS' to interact and validate a brazilian CEP
        """
        pass

    @staticmethod
    def remove_mask(cep):
        """
        Remove the mask from a CEP if it exists
        """
        return cep.translate ({ord(c): "" for c in "-"})

    @staticmethod
    def input_mask(cep):
        """
        Input mask a CEP
        """
        return "%s-%s" % (cep[0:5], cep[5:8])

    @staticmethod
    def format(cep, use_mask=False):
        """
        Method that formats a brazilian CEP

        :param use_mask: Define if CEP use MASK or not

        Tests:
        print Cep.format('03639-040')
        03639040

        Tests (before call this function, you need ensure that "len(CEP) == 8"):
        print Cep.format('03639040', use_mask=True)
        03639-040
        """
        if use_mask:
            return Cep.input_mask(cep)
        return Cep.remove_mask(cep)

    @staticmethod
    def validate(cep):
        """
        Tests:

        print Cep.validate('03639-040')
        True

        print Cep.validate('03639')
        print Cep.validate('3639040')
        print Cep.validate('040')
        False
        """
        regex = re.compile(r"(\b\d{5}-\d{3}\b)")

        if re.findall(regex, cep):
            return True
        return False
