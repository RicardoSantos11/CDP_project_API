class Cpf:

    def __init__(self):
        """
        'CLASS' to interact and validate a brazilian CPF
        """
        pass

    @staticmethod
    def remove_mask(cpf):
        """
        Remove the mask from a CPF if it exists
        """
        return cpf.translate ({ord(c): "" for c in ".-"})

    @staticmethod
    def input_mask(cpf):
        """
        Input mask a CPF
        """
        return "%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

    @staticmethod
    def format(cpf, use_mask=False):
        """
        Method that formats a brazilian CPF

        :param use_mask: Define if CPF use MASK or not

        Tests:
        print Cpf.format('912.890.377-36')
        91289037736

        Tests (before call this function, you need ensure that "len(CPF) == 11"):
        print Cpf.format('91289037736', use_mask=True)
        912.890.377-36
        """
        if use_mask:
            return Cpf.input_mask(cpf)
        return Cpf.remove_mask(cpf)

    @staticmethod
    def validate(cpf):
        """
        Tests:
        print Cpf.validate('91289037736')
        True

        print Cpf.validate('91289037731')
        False
        """
        if len(cpf) == 11:
            cpf_invalidos = [11 * str(i) for i in range(10)]
            if cpf in cpf_invalidos:
                return False

            if not cpf.isdigit():
                """Checks for special characters"""
                cpf = Cpf.remove_mask(cpf)

            """Checking CPF"""
            selfcpf = [int(x) for x in cpf]

            cpf = selfcpf[:9]

            while len(cpf) < 11:
                r = sum([(len(cpf) + 1 - i) * v for i, v in [(x, cpf[x]) for x in range(len(cpf))]]) % 11

                if r > 1:
                    f = 11 - r
                else:
                    f = 0
                cpf.append(f)

            return bool(cpf == selfcpf)

        return False
