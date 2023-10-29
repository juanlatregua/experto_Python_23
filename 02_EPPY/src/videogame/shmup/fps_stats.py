from shmup.config import cfg_item
from shmup.assets.assetmanager import AssetManager

class FPSStats:

    def __init__(self):
        self.__logic_frames = 0
        self.__render_frames = 0
        self.__set_fps_surface()
        self.__update_time = 0

    def update(self, delta_time):
        self.__logic_frames += 1
        self.__update_time += delta_time

        if self.__update_time >= cfg_item("timing","refresh_stats_time"):
            self.__set_fps_surface()
            self.__logic_frames = 0
            self.__render_frames = 0
            self.__update_time -= cfg_item("timing","refresh_stats_time")

    def render(self, surface_dst):
        self.__render_frames += 1
        surface_dst.blit(self.__image, cfg_item("timing","fps_pos"))

    def __set_fps_surface(self):
        font = AssetManager.instance().get(cfg_item("font", "name"))
        self.__image = font.render(f"{self.__logic_frames} - {self.__render_frames}", True, cfg_item("game", "foreground_color"), None)
