import igl
import polyscope as ps

V,F = igl.read_triangle_mesh("BUG.ply")

ps.init()

ps.register_surface_mesh("My Bug", V, F)

ps.show()