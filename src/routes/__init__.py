from fastapi.routing import APIRoute
from .clx_routes import route as clx_rt
from .mat_routes import route as mat_rt

lst_routers = [clx_rt, mat_rt]

#for router in lst_routers:
#    for route in router.routes:
#            if isinstance(route, APIRoute): 
#                print(f"Methods: {route.methods} | Path: {route.path}")

