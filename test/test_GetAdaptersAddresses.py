captions = ['Adapter Name', 'Dns Suffix', 'Description', 'Friendly Name', 'Physical Address (MAC)', 'Physical Address Length', 'Flags', 'Mtu', 'If Type', 'Oper Status', 'Ipv6IfIndex', 'ZoneIndices']

from pywingui.windows import *
from pywingui.wtl import *
from pywingui import comctl
from pywingui.lib import form
from pywingui.error import NO_ERROR, ERROR_NO_DATA

from pywingui.network.iphlpapi import GetAdaptersAddresses
from pywingui.network.ipifcons import *
from pywingui.network.iptypes import GAA_FLAG_SKIP_UNICAST, GAA_FLAG_SKIP_ANYCAST, GAA_FLAG_SKIP_MULTICAST, GAA_FLAG_SKIP_DNS_SERVER

comctl.InitCommonControls(comctl.ICC_USEREX_CLASSES)

class Form(form.Form):
	_form_menu_ = [(MF_POPUP, '&File', [(MF_STRING, '&Exit', form.ID_EXIT)])]
	_window_title_ = 'GetAdaptersAddresses Example'

	def __init__(self, *args, **kwargs):
		form.Form.__init__(self, *args, **kwargs)      
		#~ self.list_view.SetItemCount(len(captions))
		#~ self.list_view.SetRedraw(1)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 150, 'item')
		self.list_view.InsertColumn(0, lvcolumn)
		lvcolumn = comctl.LVCOLUMN(comctl.LVCF_TEXT|comctl.LVCF_WIDTH, 0, 350, 'value')
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
		#~ dwRetval, adapter_addresses, size = GetAdaptersAddresses(family = GAA_FLAG_SKIP_UNICAST | GAA_FLAG_SKIP_ANYCAST | GAA_FLAG_SKIP_MULTICAST | GAA_FLAG_SKIP_DNS_SERVER, flags = 2)#AF_INET)
		dwRetval, adapter_addresses, size = GetAdaptersAddresses(0, 0, None)
		if dwRetval != NO_ERROR:
			print('Call to GetAdaptersAddresses failed with error: %d' % dwRetval)
			if dwRetval == ERROR_NO_DATA:
				print('No addresses were found for the requested parameters')
			else:
				print('Error description: "%s"' % FormatError(dwRetval))
		else:
			items[0].pszText = adapter_addresses.AdapterName
			items[1].pszText = adapter_addresses.DnsSuffix
			items[2].pszText = adapter_addresses.Description
			items[3].pszText = adapter_addresses.FriendlyName
			physical_address_as_string, i = '', 0
			if adapter_addresses.PhysicalAddressLength:
				for value in adapter_addresses.PhysicalAddress:# MAC Address
					if i <= adapter_addresses.PhysicalAddressLength:
						physical_address_as_string += '%.2X-' % value
					else:
						physical_address_as_string += '%.2X' % value
					i += 1
			items[4].pszText = physical_address_as_string
			items[5].pszText = '%d' % adapter_addresses.PhysicalAddressLength
			items[6].pszText = '%d' % adapter_addresses.Flags
			items[7].pszText = '%d' % adapter_addresses.Mtu
			type_as_string = 'Unknown type %d' % adapter_addresses.IfType
			if adapter_addresses.IfType == MIB_IF_TYPE_OTHER:
				type_as_string = 'Other'
			elif adapter_addresses.IfType == MIB_IF_TYPE_ETHERNET:
				type_as_string = 'Ethernet'
			elif adapter_addresses.IfType == MIB_IF_TYPE_TOKENRING:
				type_as_string = 'Token Ring'
			elif adapter_addresses.IfType == MIB_IF_TYPE_FDDI:
				type_as_string = 'FDDI'
			elif adapter_addresses.IfType ==  MIB_IF_TYPE_PPP:
				type_as_string = 'PPP'
			elif adapter_addresses.IfType ==  MIB_IF_TYPE_LOOPBACK:
				type_as_string = 'Lookback'
			elif adapter_addresses.IfType ==  MIB_IF_TYPE_SLIP:
				type_as_string = 'Slip'
			items[8].pszText = type_as_string
			items[9].pszText = '%d' % adapter_addresses.OperStatus
			items[10].pszText = '%d' % adapter_addresses.Ipv6IfIndex
			items[11].pszText = ''.join(['%d' % value for value in adapter_addresses.ZoneIndices])
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
