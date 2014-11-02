def EuAg(Big, Small):
        if (Big%Small==0):
                return Small
        else:
                return EuAg(Small, Big%Small)



