import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class SleepNode(Node, ArmLogicTreeNode):
    '''Sleep node'''
    bl_idname = 'LNSleepNode'
    bl_label = 'Sleep'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('NodeSocketShader', "In")
        self.inputs.new('NodeSocketFloat', "Time")
        self.outputs.new('NodeSocketShader', "Out")

add_node(SleepNode, category='Operator')