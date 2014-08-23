#
# Conditional build:
%bcond_with	hal	# use HAL for hotplugging
#
Summary:	PC/SC driver for Gemalto/Axalto/Schlumberger e-gate adapters
Summary(pl.UTF-8):	Sterownik PC/SC dla adapterów kart e-gate firmy Gemalto/Axalto/Schlumberger
Name:		pcsc-driver-egate
Version:	0.90
Release:	1
License:	BSD or LGPL v2+
Group:		Libraries
Source0:	http://dl.central.org/dl/software/ifd-egate/ifd-egate-%{version}.tar.gz
# Source0-md5:	3d186fedeff6fd4f4e93db94cc6cb80d
%{?with_hal:BuildRequires:	hal-devel}
BuildRequires:	libusb-compat-devel >= 0.1
BuildRequires:	pcsc-lite-devel >= 1.3.3
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
Requires:	pcsc-lite >= 1.3.3
Obsoletes:	ifd-egate
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		usbdropdir	/usr/%{_lib}/pcsc/drivers

%description
This package provides a smart card reader driver for the
Gemalto/Axalto/Schlumberger e-gate adapters for e-gate compatible
cards for use with pcsc-lite.

%description -l pl.UTF-8
Ten pakiet zawiera sterownik czytników kart procesorowych dla
adapterów e-gate firmy Gemalto/Axalto/Schlumberger dla kart zgodnych
z e-gate, przeznaczony do użycia z pcsc-lite.

%prep
%setup -q -n ifd-egate-%{version}

%build
%configure \
	%{!?with_hal:--disable-libhal}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NEWS PROTOCOL README
%dir %{usbdropdir}/egate.bundle
%dir %{usbdropdir}/egate.bundle/Contents
%{usbdropdir}/egate.bundle/Contents/Info.plist
%dir %{usbdropdir}/egate.bundle/Contents/Linux
%attr(755,root,root) %{usbdropdir}/egate.bundle/Contents/Linux/libifd_egate.so*
