from ev3sim.logging import Logger
import pygame
import pygame_gui
from pygame_gui.core.ui_element import ObjectID
from ev3sim.visual.menus.base_menu import BaseMenu


class SimulatorMenu(BaseMenu):

    ROBOT_COLOURS = [
        "#ff006e",
        "#02c39a",
        "#deaaff",
        "#ffbe0b",
    ]

    ERROR_COLOUR = "#d90429"

    def initWithKwargs(self, **kwargs):
        batch = kwargs.get("batch")
        from ev3sim.simulation.loader import StateHandler
        from ev3sim.simulation.world import World

        World.instance.resetWorld()

        StateHandler.instance.beginSimulation(batch=batch)
        self.messages = []
        super().initWithKwargs(**kwargs)

    def onPop(self):
        from ev3sim.simulation.loader import StateHandler, ScriptLoader

        # We need to close all previous communications with the bots.
        StateHandler.instance.closeProcesses()
        StateHandler.instance.is_simulating = False
        # We also need to reset the objects registered to the Screen.
        from ev3sim.visual.manager import ScreenObjectManager

        ScreenObjectManager.instance.resetVisualElements()
        # We also need to reset the physics sim.
        from ev3sim.simulation.world import World

        World.instance.resetWorld()
        # And reset the script loader.
        ScriptLoader.instance.reset()

    def generateObjects(self):
        dummy_rect = pygame.Rect(0, 0, *self._size)
        self.console_bg = pygame_gui.elements.UIPanel(
            relative_rect=dummy_rect, starting_layer_height=0.5, manager=self, object_id=ObjectID("console-bg")
        )
        self._all_objs.append(self.console_bg)
        self.gen_messages = []
        self.current_y = 0
        for i, (_, __, msg) in enumerate(self.messages):
            self.gen_messages.append(
                pygame_gui.elements.UITextBox(
                    html_text=msg,
                    relative_rect=pygame.Rect(0, self.current_y, self._size[0] / 2, -1),
                    manager=self,
                    object_id=ObjectID(f"console-text-{i}", "console-text"),
                )
            )
            self.current_y += self.gen_messages[-1].rect.height
        self._all_objs.extend(self.gen_messages)

    def sizeObjects(self):
        self.console_bg.set_position((0, 0))
        self.console_bg.set_dimensions((self._size[0] / 2, self.current_y))

    def printMessage(self, msg, msg_life=3, kill=True):
        for i, col in enumerate(self.ROBOT_COLOURS):
            repl = f"[Robot-{i}]"
            msg = msg.replace("\n", "<br>")
            msg = msg.replace(repl, f'<font color="{col}">{repl}</font>')
        self.messages.append([kill, msg_life, msg])
        self.regenerateObjects()

    def printError(self, robot_index):
        actual_msg = (
            f'<font color="{self.ROBOT_COLOURS[robot_index]}">Robot-{robot_index}</font> '
            + f'<font color="{self.ERROR_COLOUR}">ran into an error!<br>'
            + f"Click <a href='restart-{robot_index}'>here</a> to restart the bot.<br>"
            + f"Click <a href='logs-{robot_index}'>here</a> to view the error log."
            + "</font>"
        )
        # The robot index here lets us find and remove the message.
        self.messages.append([False, robot_index, actual_msg])
        self.regenerateObjects()

    def update(self, time_delta: float):
        super().update(time_delta)
        to_remove = []
        for i in range(len(self.messages)):
            if self.messages[i][0]:
                self.messages[i][1] -= time_delta
                if self.messages[i][1] < 0:
                    to_remove.append(i)
        for index in to_remove[::-1]:
            del self.messages[index]
        if len(to_remove) != 0:
            self.regenerateObjects()

    def handleEvent(self, event):
        if hasattr(event, "link_target"):
            if event.link_target.startswith("restart"):
                from ev3sim.simulation.loader import ScriptLoader

                robot_index = int(event.link_target.split("-")[1])
                for i in range(len(self.messages)):
                    if not self.messages[i][0] and self.messages[i][1] == robot_index:
                        del self.messages[i]
                        break
                self.regenerateObjects()
                ScriptLoader.instance.startProcess(f"Robot-{robot_index}")
            elif event.link_target.startswith("logs"):
                robot_index = int(event.link_target.split("-")[1])
                Logger.instance.openLog(f"Robot-{robot_index}")
