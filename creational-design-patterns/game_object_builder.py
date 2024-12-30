class GameObject:
  def __init__(self):
    self.transform = None
    self.renderer = None
    self.collider = None
    self.script = None

  def __str__(self):
    return f"Transform: {self.transform} | Renderer: {self.renderer} | Collider: {self.collider} | Script: {self.script}"
  
class GameBuilder:
  def __init__(self):
    self._game = GameObject()

  def add_transform(self, position, rotation, scale):
    self._game.transform = Transform(position, rotation, scale)

  def add_renderer(self, material, mesh):
    self._game.renderer = Renderer(material, mesh)

  def add_collider(self, shape, is_trigger):
    self._game.collider = Collider(shape, is_trigger)

  def add_script(self, script):
    self._game.script = script

  def get_game(self):
    return self._game
  
class Transform:
  def __init__(self, position, rotation, scale):
    self.position = position
    self.rotation = rotation
    self.scale = scale

  def __str__(self):
    return f"Position: {self.position} | Rotation: {self.rotation} | Scale: {self.scale}"
  
class Renderer:
  def __init__(self, material, mesh):
    self.material = material
    self.mesh = mesh

  def __str__(self):
    return f"Material: {self.material} | Mesh: {self.mesh}"
  
class Collider:
  def __init__(self, shape, is_trigger):
    self.shape = shape
    self.is_trigger = is_trigger

  def __str__(self):
    return f"Shape: {self.shape} | Is Trigger: {self.is_trigger}"
  
if __name__ == "__main__":
  print("=======ENGINE 1============")
  builder = GameBuilder()
  builder.add_transform((1,2,3),(4,6,2),(5,6,2))
  builder.add_renderer("CubeMesh","DefaultBlackShine")
  builder.add_collider("Box", False)
  builder.add_script("TurnScript.js")

  game = builder.get_game()
  print(game)


  print("=======ENGINE 2============")
  builder2 = GameBuilder()
  builder2.add_transform((10,12,23),(5,22,15),(14,9,7))
  builder2.add_renderer("Cylinder", "DarkCloud")
  builder2.add_collider("Circlic", True)
  builder2.add_script("ManualTurner")
  game = builder2.get_game()
  print(game) 