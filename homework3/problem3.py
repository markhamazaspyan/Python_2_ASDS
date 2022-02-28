"""Use singleton pattern and classes of your choice. Create a structure where you have some resource
that has states busy and free and 3 users that try to use the resource and change the state to busy
while they are using it. The resource should be singleton. Implement using 2 different methods for
singleton implementation that we have discussed.
"""



class BorgResource:
    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = "free"

    def use_resource(self):
        self.state = "busy"


class ClassicResource:
    __shared_instance = 'free'

    @staticmethod
    def getInstance():

        """Static Access Method"""
        if ClassicResource.__shared_instance == 'free':
            ClassicResource()
        return ClassicResource.__shared_instance

    def __init__(self):

        if ClassicResource.__shared_instance != 'free':
            raise Exception("State is busy.")
        else:
            ClassicResource.__shared_instance = self

    def use_resource(self):
        print('Using the resource')



if __name__ == "__main__":
    print("Borg Singleton")
    user1=BorgResource()
    user2=BorgResource()
    user3=BorgResource()
    print("user1:", user1.state)
    user1.use_resource()
    print("user1:", user1.state)
    print("user2:", user2.state)
    print("user3:", user3.state)

    print("\n", )
    print("Classic Singleton")
    user1 = ClassicResource()
    user1.use_resource()
    user2 = ClassicResource()
