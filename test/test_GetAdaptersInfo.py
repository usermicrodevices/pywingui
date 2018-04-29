captions = ['Combo Index', 'Adapter Name', 'Description', 'Address Length', 'Address (MAC)', 'Index', 'Type', 'Dhcp Enabled', 'Current Ip Address', 'Ip Address List', 'Gateway List', 'Dhcp Server', 'Have Wins', 'Primary Wins Server', 'Secondary Wins Server', 'Lease Obtained', 'Lease Expires']

from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl
from pywingui.lib import form
from pywingui.error import NO_ERROR

from pywingui.network.iphlpapi import GetAdaptersInfo
from pywingui.network.ipifcons import *

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]
	_window_title_ = 'GetAdaptersInfo Example'

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)      
		#~ self.list_view.SetItemCount(len(captions))
		#~ self.list_view.SetRedraw(1)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 120, 'item')
		self.list_view.InsertColumn(0, lvcolumn)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 400, 'value')
		self.list_view.InsertColumn(1, lvcolumn)
		item_flags = comctl.LVIF_TEXT|comctl.LVIF_DI_SETITEM
		items = []
		for i in range(len(captions)):
			item = comctl.LVITEM(item_flags)
			item.iItem = i
			item.pszText = captions[i]
			self.list_view.InsertItem(item)
			# now setup second column of current row, change iSubItem
			item.iSubItem = 1
			item.pszText = 'value %d' % i
			self.list_view.SetItem(item)
			items.append(item)
		dwRetval, adapter_info, size = GetAdaptersInfo()
		if dwRetval != NO_ERROR:
			print('GetAdaptersInfo call failed with %d' % dwRetval)
		else:
			items[0].pszText = '%d' % adapter_info.ComboIndex
			items[1].pszText = adapter_info.AdapterName
			items[2].pszText = adapter_info.Description
			items[3].pszText = '%d' % adapter_info.AddressLength
			physical_address_as_string, i = '', 0
			for value in adapter_info.Address:# MAC Address
				if i <= adapter_info.AddressLength:
					physical_address_as_string += '%.2X-' % value
				else:
					physical_address_as_string += '%.2X' % value
				i += 1
			items[4].pszText = physical_address_as_string
			items[5].pszText = '%d' % adapter_info.Index
			type_as_string = 'Unknown type %d' % adapter_info.Type
			if adapter_info.Type == MIB_IF_TYPE_OTHER:
				type_as_string = 'Other'
			elif adapter_info.Type == MIB_IF_TYPE_ETHERNET:
				type_as_string = 'Ethernet'
			elif adapter_info.Type == MIB_IF_TYPE_TOKENRING:
				type_as_string = 'Token Ring'
			elif adapter_info.Type == MIB_IF_TYPE_FDDI:
				type_as_string = 'FDDI'
			elif adapter_info.Type ==  MIB_IF_TYPE_PPP:
				type_as_string = 'PPP'
			elif adapter_info.Type ==  MIB_IF_TYPE_LOOPBACK:
				type_as_string = 'Lookback'
			elif adapter_info.Type ==  MIB_IF_TYPE_SLIP:
				type_as_string = 'Slip'
			items[6].pszText = type_as_string
			items[7].pszText = '%d' % adapter_info.DhcpEnabled
			#~ items[8].pszText = adapter_info.CurrentIpAddress[0].IpAddress.String
			items[8].pszText = repr(adapter_info.CurrentIpAddress)
			items[9].pszText = adapter_info.IpAddressList.IpAddress.String
			items[10].pszText = adapter_info.GatewayList.IpAddress.String
			items[11].pszText = adapter_info.DhcpServer.IpAddress.String
			items[12].pszText = repr(adapter_info.HaveWins)
			items[13].pszText = adapter_info.PrimaryWinsServer.IpAddress.String
			items[14].pszText = adapter_info.SecondaryWinsServer.IpAddress.String
			items[15].pszText = '%d' % adapter_info.LeaseObtained
			items[16].pszText = '%d' % adapter_info.LeaseExpires
			for item in items:
				self.list_view.SetItem(item)

	def OnCreate(self, event):
		self.list_view = comctl.ListView(parent = self, rcPos = RECT(5, 10, 200, 100, orExStyle = WS_EX_CLIENTEDGE))
		self.controls.Add(form.CTRL_VIEW, self.list_view)
		self.controls.Add(form.CTRL_STATUSBAR, comctl.StatusBar(parent = self))

if __name__ == '__main__':
	mainForm = Form(rcPos = RECT(0, 0, 550, 350))
	mainForm.ShowWindow()

	application = Application()
	application.Run()
