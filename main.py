from cmd_parser import cmd_parse
from commands import *
import multiprocessing as mp
from queue import Empty
import threading, time
from router import RouterStateType

baseNodeColor = (255, 255, 155)
WHITE = (255, 255, 255)
selectedNodeColor = (155, 250, 155)
routeNodeColor = (255, 100, 100)
ws = 700  # render window size


def display(display_queue: mp.Queue):
    import pygame
    pygame.init()
    sc = pygame.display.set_mode((ws, ws))
    sc.fill(WHITE)
    side_length = 30
    font = pygame.font.Font(None, 36)
    display_queue.put('init')

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                return

        try:
            [rml, edge_list]  = display_queue.get(timeout=0.2)  # rml means routers_meta_list
            #draw connections
            for edges in edge_list:
                pygame.draw.line(sc, (0, 0, 0), (ws * rml[edges[0]].x + side_length//2, ws * rml[edges[0]].y + side_length//2),
                                 (ws * rml[edges[1]].x+side_length//2, ws * rml[edges[1]].y+side_length//2), 3
                )
            #draw rect
            for meta in rml:
                router_color = baseNodeColor
                if meta.state == RouterStateType.FinishNode:
                    router_color = routeNodeColor
                elif meta.state == RouterStateType.Transits:
                    router_color = selectedNodeColor

                pygame.draw.circle(sc, router_color,
                                   (int(meta.x * ws + side_length / 2), int(meta.y * ws + side_length / 2)),
                                   20)
                pygame.draw.circle(sc, (0, 0, 0),
                                   (int(meta.x * ws + side_length / 2), int(meta.y * ws + side_length / 2)),
                                   20, 3)

                text = font.render(str(meta.id), 1, (0, 0, 0))
                sc.blit(text, (int(meta.x * ws + side_length // 3.5), int(meta.y * ws + side_length // 6)))
        except Empty:
            pass

        pygame.display.update()

key = ''
read_input = False

def input_thread():
    global key
    global read_input
    lock = threading.Lock()
    while True:
        with lock:
            key = input()
            read_input = True
            if key.__eq__('exit'):
                break

if __name__ == "__main__":
    net = Net()
    display_queue = mp.Queue()  # for update display
    display_process = mp.Process(target=display, args=(display_queue,))
    display_process.start()
    display_queue.get()  # waiting for pygame loads in display process

    input_thread = threading.Thread(target=input_thread)
    input_thread.start()

    while True:
        if read_input and key != '':
            read_input = False
            action = cmd_parse(key)
            if action.cmdType == CMD_TYPE.Exit:
                break
            action.start(net)

        routers_meta_list = []
        net.update_states()
        for router in net.routers.values():
            routers_meta_list.insert(router.meta.id, router.meta)

        display_queue.put([routers_meta_list, net.edge_list])

        time.sleep(0.3)

    display_process.terminate()
    net.terminate()