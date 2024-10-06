from solid2.core.object_base import OpenSCADConstant as _OpenSCADConstant
from solid2.core.scad_import import extra_scad_include as _extra_scad_include
from pathlib import Path as _Path

from .bosl2_base import Bosl2Base as _Bosl2Base

_extra_scad_include(f"{_Path(__file__).parent.parent / 'bosl2/BOSL2/threading.scad'}", False)

class threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, starts=None, shape=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, id1=None, id2=None, ibevel1=None, ibevel2=None, ibevel=None, bevang=None, thickness=None, height=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "starts" : starts, "shape" : shape, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "id1" : id1, "id2" : id2, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "ibevel" : ibevel, "bevang" : bevang, "thickness" : thickness, "height" : height, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class trapezoidal_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, thread_angle=None, thread_depth=None, flank_angle=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("trapezoidal_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "thread_angle" : thread_angle, "thread_depth" : thread_depth, "flank_angle" : flank_angle, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class trapezoidal_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, thread_angle=None, thread_depth=None, shape=None, flank_angle=None, left_handed=None, starts=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel1=None, ibevel2=None, ibevel=None, thickness=None, height=None, id1=None, id2=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("trapezoidal_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "thread_angle" : thread_angle, "thread_depth" : thread_depth, "shape" : shape, "flank_angle" : flank_angle, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "ibevel" : ibevel, "thickness" : thickness, "height" : height, "id1" : id1, "id2" : id2, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class acme_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, tpi=None, pitch=None, starts=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("acme_threaded_rod", {"d" : d, "l" : l, "tpi" : tpi, "pitch" : pitch, "starts" : starts, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class acme_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, tpi=None, pitch=None, starts=None, left_handed=None, shape=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("acme_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "tpi" : tpi, "pitch" : pitch, "starts" : starts, "left_handed" : left_handed, "shape" : shape, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class npt_threaded_rod(_Bosl2Base):
    def __init__(self, size=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, hollow=None, internal=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("npt_threaded_rod", {"size" : size, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "hollow" : hollow, "internal" : internal, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class buttress_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, starts=None, bevel=None, bevel1=None, bevel2=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("buttress_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class buttress_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, shape=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, bevang=None, starts=None, ibevel=None, ibevel1=None, ibevel2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("buttress_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "shape" : shape, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "starts" : starts, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class square_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("square_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class square_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, starts=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("square_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "starts" : starts, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ball_screw_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, ball_diam=None, ball_arc=None, starts=None, left_handed=None, internal=None, length=None, h=None, height=None, bevel=None, bevel1=None, bevel2=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ball_screw_rod", {"d" : d, "l" : l, "pitch" : pitch, "ball_diam" : ball_diam, "ball_arc" : ball_arc, "starts" : starts, "left_handed" : left_handed, "internal" : internal, "length" : length, "h" : h, "height" : height, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, profile=None, left_handed=None, internal=None, bevel=None, bevel1=None, bevel2=None, starts=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "profile" : profile, "left_handed" : left_handed, "internal" : internal, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, profile=None, shape=None, left_handed=None, starts=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, id1=None, id2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "profile" : profile, "shape" : shape, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "id1" : id1, "id2" : id2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class thread_helix(_Bosl2Base):
    def __init__(self, d=None, pitch=None, thread_depth=None, flank_angle=None, turns=None, profile=None, starts=None, left_handed=None, internal=None, d1=None, d2=None, thread_angle=None, lead_in_shape=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, lead_in_sample=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("thread_helix", {"d" : d, "pitch" : pitch, "thread_depth" : thread_depth, "flank_angle" : flank_angle, "turns" : turns, "profile" : profile, "starts" : starts, "left_handed" : left_handed, "internal" : internal, "d1" : d1, "d2" : d2, "thread_angle" : thread_angle, "lead_in_shape" : lead_in_shape, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "lead_in_sample" : lead_in_sample, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, starts=None, shape=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, id1=None, id2=None, ibevel1=None, ibevel2=None, ibevel=None, bevang=None, thickness=None, height=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "starts" : starts, "shape" : shape, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "id1" : id1, "id2" : id2, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "ibevel" : ibevel, "bevang" : bevang, "thickness" : thickness, "height" : height, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class trapezoidal_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, thread_angle=None, thread_depth=None, flank_angle=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("trapezoidal_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "thread_angle" : thread_angle, "thread_depth" : thread_depth, "flank_angle" : flank_angle, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class trapezoidal_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, thread_angle=None, thread_depth=None, shape=None, flank_angle=None, left_handed=None, starts=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel1=None, ibevel2=None, ibevel=None, thickness=None, height=None, id1=None, id2=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("trapezoidal_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "thread_angle" : thread_angle, "thread_depth" : thread_depth, "shape" : shape, "flank_angle" : flank_angle, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "ibevel" : ibevel, "thickness" : thickness, "height" : height, "id1" : id1, "id2" : id2, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class acme_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, tpi=None, pitch=None, starts=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("acme_threaded_rod", {"d" : d, "l" : l, "tpi" : tpi, "pitch" : pitch, "starts" : starts, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class acme_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, tpi=None, pitch=None, starts=None, left_handed=None, shape=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("acme_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "tpi" : tpi, "pitch" : pitch, "starts" : starts, "left_handed" : left_handed, "shape" : shape, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class npt_threaded_rod(_Bosl2Base):
    def __init__(self, size=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, hollow=None, internal=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("npt_threaded_rod", {"size" : size, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "hollow" : hollow, "internal" : internal, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class buttress_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, starts=None, bevel=None, bevel1=None, bevel2=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("buttress_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class buttress_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, shape=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, bevang=None, starts=None, ibevel=None, ibevel1=None, ibevel2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("buttress_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "shape" : shape, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "starts" : starts, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class square_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, starts=None, internal=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("square_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "internal" : internal, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class square_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, left_handed=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, starts=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("square_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "left_handed" : left_handed, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "starts" : starts, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ball_screw_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, ball_diam=None, ball_arc=None, starts=None, left_handed=None, internal=None, length=None, h=None, height=None, bevel=None, bevel1=None, bevel2=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ball_screw_rod", {"d" : d, "l" : l, "pitch" : pitch, "ball_diam" : ball_diam, "ball_arc" : ball_arc, "starts" : starts, "left_handed" : left_handed, "internal" : internal, "length" : length, "h" : h, "height" : height, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_threaded_rod(_Bosl2Base):
    def __init__(self, d=None, l=None, pitch=None, profile=None, left_handed=None, internal=None, bevel=None, bevel1=None, bevel2=None, starts=None, d1=None, d2=None, length=None, h=None, height=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_threaded_rod", {"d" : d, "l" : l, "pitch" : pitch, "profile" : profile, "left_handed" : left_handed, "internal" : internal, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "starts" : starts, "d1" : d1, "d2" : d2, "length" : length, "h" : h, "height" : height, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class generic_threaded_nut(_Bosl2Base):
    def __init__(self, nutwidth=None, id=None, h=None, pitch=None, profile=None, shape=None, left_handed=None, starts=None, bevel=None, bevel1=None, bevel2=None, bevang=None, ibevel=None, ibevel1=None, ibevel2=None, id1=None, id2=None, height=None, thickness=None, length=None, l=None, blunt_start=None, blunt_start1=None, blunt_start2=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, end_len=None, end_len1=None, end_len2=None, lead_in_shape=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("generic_threaded_nut", {"nutwidth" : nutwidth, "id" : id, "h" : h, "pitch" : pitch, "profile" : profile, "shape" : shape, "left_handed" : left_handed, "starts" : starts, "bevel" : bevel, "bevel1" : bevel1, "bevel2" : bevel2, "bevang" : bevang, "ibevel" : ibevel, "ibevel1" : ibevel1, "ibevel2" : ibevel2, "id1" : id1, "id2" : id2, "height" : height, "thickness" : thickness, "length" : length, "l" : l, "blunt_start" : blunt_start, "blunt_start1" : blunt_start1, "blunt_start2" : blunt_start2, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "end_len" : end_len, "end_len1" : end_len1, "end_len2" : end_len2, "lead_in_shape" : lead_in_shape, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _nutshape(_Bosl2Base):
    def __init__(self, nutwidth=None, h=None, shape=None, bevel1=None, bevel2=None, **kwargs):
       super().__init__("_nutshape", {"nutwidth" : nutwidth, "h" : h, "shape" : shape, "bevel1" : bevel1, "bevel2" : bevel2, **kwargs})

class thread_helix(_Bosl2Base):
    def __init__(self, d=None, pitch=None, thread_depth=None, flank_angle=None, turns=None, profile=None, starts=None, left_handed=None, internal=None, d1=None, d2=None, thread_angle=None, lead_in_shape=None, lead_in=None, lead_in1=None, lead_in2=None, lead_in_ang=None, lead_in_ang1=None, lead_in_ang2=None, lead_in_sample=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("thread_helix", {"d" : d, "pitch" : pitch, "thread_depth" : thread_depth, "flank_angle" : flank_angle, "turns" : turns, "profile" : profile, "starts" : starts, "left_handed" : left_handed, "internal" : internal, "d1" : d1, "d2" : d2, "thread_angle" : thread_angle, "lead_in_shape" : lead_in_shape, "lead_in" : lead_in, "lead_in1" : lead_in1, "lead_in2" : lead_in2, "lead_in_ang" : lead_in_ang, "lead_in_ang1" : lead_in_ang1, "lead_in_ang2" : lead_in_ang2, "lead_in_sample" : lead_in_sample, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

