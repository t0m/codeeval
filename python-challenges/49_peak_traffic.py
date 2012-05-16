import sys

everyone = {}

class Friend():
    def __init__(self, email):
        self.email = email
        self.friends = set([self])
        self.buddies = set([self])

    def add_friend(self, friend):
        if self in friend.friends:
            self.buddies.add(friend)
            friend.buddies.add(self)
        self.friends.add(friend)
    
    def __str__(self):
        return self.email


def build_cluster(buddies):
    reachable = []
    for buddy in buddies:
        reachable.append(buddy.buddies)
    
    return set.intersection(*reachable)


if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            date, my_email, friends_email = line.strip().split('\t')

            me = everyone.get(my_email)
            friend = everyone.get(friends_email)
            if me is None:
                me = Friend(my_email)
                everyone[my_email] = me
            if friend is None:
                friend = Friend(friends_email)
                everyone[friends_email] = friend
            me.add_friend(friend)
    
    clusters = set()
    for person in everyone.values():
        cluster_set = build_cluster(person.buddies)
        if len(cluster_set) > 2:
            clusters.add(tuple(sorted(cluster_set, key=lambda person:person.email)))
    
    for cluster in clusters:
        print ', '.join([person.email for person in cluster])

    sys.exit(0)
