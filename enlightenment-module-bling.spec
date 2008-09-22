%define		_snap		20080814
%define		module_name	bling
Summary:	Enlightenment DR17 module: %{module_name}
Summary(pl.UTF-8):	Moduł Enlightenmenta DR17: %{module_name}
Name:		enlightenment-module-%{module_name}
Version:	0.0.1
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Window Managers/Tools
Source0:	%{module_name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	6d024eb2e6a3e369346e2bb9a7793e7a
URL:		http://code.google.com/p/itask-module/wiki/ItaskNG
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	enlightenment-devel >= 0.16.999.044
BuildRequires:	gettext-autopoint
BuildRequires:	libtool
Requires:	enlightenment >= 0.16.999.044
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bling module is an xcompmgr derived, EFLized composite manager for
E17.

%description -l pl.UTF-8
Moduł Bling jest pochodnym xcompmgr zarządcą składania dla E17.

%prep
%setup -q -n %{module_name}-%{version}-%{_snap}

%build
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_libdir}/enlightenment/modules/%{module_name}
%dir %{_libdir}/enlightenment/modules/%{module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules/%{module_name}/linux-gnu-*/module.so
%{_libdir}/enlightenment/modules/%{module_name}/module.desktop
%{_libdir}/enlightenment/modules/%{module_name}/*.edj
