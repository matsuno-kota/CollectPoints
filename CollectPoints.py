#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file CollectPoints.py
 @brief collect points
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
collectpoints_spec = ["implementation_id", "CollectPoints",
		 "type_name",         "CollectPoints",
		 "description",       "collect points",
		 "version",           "1.0.0",
		 "vendor",            "Kota Matsuno",
		 "category",          "test",
		 "activity_type",     "STATIC",
		 "max_instance",      "1",
		 "language",          "Python",
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class CollectPoints
# @brief collect points
#
#
class CollectPoints(OpenRTM_aist.DataFlowComponentBase):

	##
	# @brief constructor
	# @param manager Maneger Object
	#
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_point1 = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._point1In = OpenRTM_aist.InPort("point1", self._d_point1)
		self._d_point2 = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._point2In = OpenRTM_aist.InPort("point2", self._d_point2)
		self._d_point3 = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._point3In = OpenRTM_aist.InPort("point3", self._d_point3)
		self._d_point = OpenRTM_aist.instantiateDataType(RTC.TimedString)
		"""
		"""
		self._pointOut = OpenRTM_aist.OutPort("point", self._d_point)





		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">

		# </rtc-template>



	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry()
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onInitialize(self):
		# Bind variables and configuration variable

		# Set InPort buffers
		self.addInPort("point1",self._point1In)
		self.addInPort("point2",self._point2In)
		self.addInPort("point3",self._point3In)

		# Set OutPort buffers
		self.addOutPort("point",self._pointOut)

		# Set service provider to Ports

		# Set service consumers to Ports

		# Set CORBA Service Ports

		return RTC.RTC_OK

	###
	##
	## The finalize action (on ALIVE->END transition)
	## formaer rtc_exiting_entry()
	##
	## @return RTC::ReturnCode_t
	#
	##
	#def onFinalize(self):
	#
	#	return RTC.RTC_OK

	###
	##
	## The startup action when ExecutionContext startup
	## former rtc_starting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The shutdown action when ExecutionContext stop
	## former rtc_stopping_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The activated action (Active state entry action)
	## former rtc_active_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onActivated(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The deactivated action (Active state exit action)
	## former rtc_active_exit()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK

	##
	#
	# The execution action that is invoked periodically
	# former rtc_active_do()
	#
	# @param ec_id target ExecutionContext Id
	#
	# @return RTC::ReturnCode_t
	#
	#
	def onExecute(self, ec_id):
		points = ""

		a = self._point1In.isNew()
		b = self._point2In.isNew()
		c = self._point3In.isNew()

		if a == True and b == True and c == True:
			point1 = self._point1In.read()
			point2 = self._point2In.read()
			point3 = self._point3In.read()
			points = str(point1.data) + "," + str(point2.data) + "," + str(point3.data)

		if not points == "":
			print(points)
			self._d_point.data = points
			self._pointOut.write()
		return RTC.RTC_OK

	###
	##
	## The aborting action when main logic error occurred.
	## former rtc_aborting_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The error action in ERROR state
	## former rtc_error_do()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The reset action that is invoked resetting
	## This is same but different the former rtc_init_entry()
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The state update action that is invoked after onExecute() action
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##

	##
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK

	###
	##
	## The action that is invoked when execution context's rate is changed
	## no corresponding operation exists in OpenRTm-aist-0.2.0
	##
	## @param ec_id target ExecutionContext Id
	##
	## @return RTC::ReturnCode_t
	##
	##
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK




def CollectPointsInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=collectpoints_spec)
    manager.registerFactory(profile,
                            CollectPoints,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    CollectPointsInit(manager)

    # Create a component
    comp = manager.createComponent("CollectPoints")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()
