Summary:	Tools for connecting joysticks & legacy devices to the kernel's input subsystem
Summary(pl.UTF-8):	Narzędzia podłączające joysticki i tradycyjne urządzenia do podsystemu wejścia jądra
Name:		linuxconsoletools
Version:	1.8.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://downloads.sourceforge.net/linuxconsole/%{name}-%{version}.tar.bz2
# Source0-md5:	e68b6f473d81715e7be836b88fff6afe
Patch0:		%{name}-awk.patch
Patch1:		%{name}-wacom.patch
URL:		https://sourceforge.net/projects/linuxconsole/
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	pkgconfig
Provides:	joystick = %{version}-%{release}
Obsoletes:	joystick < 1.2.16-1
Conflicts:	gpm < 1.20.6-26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains utilities for testing and configuring joysticks,
connecting legacy devices to the kernel's input subsystem (providing
support for serial mice, touchscreens etc.), and test the input event
layer.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia pozwalające na testowanie oraz
konfigurowanie joysticków, dołączanie tradycyjnych urządzeń do
podsystemu wejścia jądra (zapewniając obsługę szeregowych myszy,
ekranów dotykowych itp.) oraz testowanie warstwy zdarzeń wejściowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/evdev-joystick
%attr(755,root,root) %{_bindir}/ffcfstress
%attr(755,root,root) %{_bindir}/ffmvforce
%attr(755,root,root) %{_bindir}/ffset
%attr(755,root,root) %{_bindir}/fftest
%attr(755,root,root) %{_bindir}/inputattach
%attr(755,root,root) %{_bindir}/jscal
%attr(755,root,root) %{_bindir}/jscal-restore
%attr(755,root,root) %{_bindir}/jscal-store
%attr(755,root,root) %{_bindir}/jstest
%dir %{_datadir}/joystick
%attr(755,root,root) %{_datadir}/joystick/*
%attr(755,root,root) /lib/udev/js-set-enum-leds
/lib/udev/rules.d/80-stelladaptor-joystick.rules
%{_mandir}/man1/evdev-joystick.1*
%{_mandir}/man1/ffcfstress.1*
%{_mandir}/man1/ffmvforce.1*
%{_mandir}/man1/ffset.1*
%{_mandir}/man1/fftest.1*
%{_mandir}/man1/inputattach.1*
%{_mandir}/man1/jscal.1*
%{_mandir}/man1/jscal-restore.1*
%{_mandir}/man1/jscal-store.1*
%{_mandir}/man1/jstest.1*
