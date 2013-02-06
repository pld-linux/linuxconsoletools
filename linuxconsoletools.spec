Summary:	Tools for connecting joysticks & legacy devices to the kernel's input subsystem
Name:		linuxconsoletools
Version:	1.4.4
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://downloads.sourceforge.net/linuxconsole/%{name}-%{version}.tar.bz2
# Source0-md5:	4ae531759fb7b2315db941a0bea52884
Patch0:		%{name}-awk.patch
Patch1:		%{name}-wacom.patch
URL:		http://sourceforge.net/projects/linuxconsole/
BuildRequires:	SDL-devel
Provides:	joystick = %{version}-%{release}
Obsoletes:	joystick < 1.2.16-1
Conflicts:	gpm < 1.20.6-26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains utilities for testing and configuring joysticks,
connecting legacy devices to the kernel's input subsystem (providing
support for serial mice, touchscreens etc.), and test the input event
layer.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README NEWS
%dir %{_datadir}/joystick
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/joystick/*
%{_mandir}/man1/*

