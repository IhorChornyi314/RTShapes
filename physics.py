from singletones import scene


class Physics:
    def __init__(self):
        self.regions = {}

    def get_collisions(self, o):
        result = []
        world_objects = self.get_objects_in_same_regions(o)
        for world_object in world_objects:
            if o.collider.collides(world_object.collider):
                result.append(world_object)
        return result

    def get_objects_in_same_regions(self, o):
        result = []
        for region in self.regions:
            if o in self.regions[region]:
                result += self.regions[region]
                result.remove(o)
        return result

    def update_regions(self):
        pass
        # self.regions[0] =
