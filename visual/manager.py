import pygame
from typing import Dict, List, Tuple

from visual.utils import hex_to_pycolor

class ScreenObjectManager:

    instance: 'ScreenObjectManager'

    screen: pygame.Surface
    screen_width: int
    screen_height: float

    _background_color: Tuple[int]

    objects: Dict[str, 'visual.objects.IVisualElement'] # noqa: F821
    sorting_order: List[str]

    def __init__(self, **kwargs):
        ScreenObjectManager.instance = self
        self.objects = {}
        self.sorting_order = []
        self.init_from_kwargs(**kwargs)

    def init_from_kwargs(self, **kwargs):
        self.screen_width = kwargs.get('screen_width', 640)
        self.screen_height = kwargs.get('screen_height', 480)
        self.background_color = kwargs.get('background_color', '#000000')

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        if isinstance(value, str):
            self._background_color = hex_to_pycolor(value)
        else:
            self._background_color = value

    def start_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)

    def registerVisual(self, obj: 'visual.objects.IVisualElement', key) -> str: # noqa: F821
        assert key not in self.objects, f"Tried to register visual element to screen with key that is already in use: {key}"
        self.objects[key] = obj
        # It is assumed the z-value of an item will note change as time progresses,
        # so no extra checks need to be made to sorting_order.
        # NOTE: We could speed this up with a binary search, possible performance gain with many objects.
        for x in range(len(self.sorting_order)):
            if self.objects[self.sorting_order[x]].position[2] > obj.position[2]:
                self.sorting_order.insert(x, key)
        else:
            self.sorting_order.append(key)
        return key

    def unregisterVisual(self, key) -> 'visual.objects.IVisualElement': # noqa: F821
        obj = self.objects[key]
        del self.objects[key]
        # NOTE: We could speed this up with a binary search, possible performance gain with many objects.
        self.sorting_order.remove(key)
        return obj

    def registerObject(self, obj: 'objects.base.BaseObject', key) -> str: # noqa: F821
        if obj.visual is not None:
            self.registerVisual(obj.visual, key)
        for i, child in enumerate(obj.children):
            new_key = key + str(child.__class__.__name__) + str(i)
            self.registerObject(child, new_key)

    def applyToScreen(self):
        self.screen.fill(self.background_color)
        for key in self.sorting_order:
            self.objects[key].apply_to_screen()
        pygame.display.update()

    def checkForClose(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys
                sys.exit()
