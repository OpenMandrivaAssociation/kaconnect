%define name	kaconnect
%define version	1.1.1
%define release %mkrel 7

Name: 	 	%{name}
Summary: 	QT frontend for ALSA sequencer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://www.suse.de/~mana/kalsatools.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	qt3-devel libalsa-devel
Patch1:		kaconnect-build-x86-64.patch
Patch2:		kaconnect-1.1.1-fix-build.patch

%description
Kaconnect is a QT version of the aconnect utility for the  ALSA  sequencer
system.

%prep
%setup -q
perl -p -i -e "s/gcc/gcc\ $RPM_OPT_FLAGS/g" make_kaconnect
%ifarch x86_64
%patch1 -p1 -b build64
%endif
%patch2 -p1
%build
%make -f make_kaconnect
										
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp %name $RPM_BUILD_ROOT/%_bindir

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=KAConnect
Comment=ALSA connections
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Sequencer;X-MandrivaLinux-Multimedia-Sound;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc README THANKS
%{_bindir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop



