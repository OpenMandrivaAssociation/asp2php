%define	name	asp2php
%define	version	0.77.1
%define	release	%mkrel 4


Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Program for converting .asp files to .php files
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
URL:		http://asp2php.naken.cc/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
asp2php is a program which can help you convert Micro$oft (tm) Active Server
Pages (tm) to PHP files.

Install this if you intend to migrate from Micro$oft(tm) Internet Information
Server(tm) to PHP.

%package -n gtkasp2php
Summary:	Graphical front-end for asp2php
Group:		Development/Other
License:	GPL
Requires:	asp2php
BuildRequires:	gtk+-devel >= 1.2.0

%description -n gtkasp2php
gtkasp2php is the gtk-based graphical front-end for asp2php.

Install this if you want a graphical front-end for asp2php.

%prep
%setup -q 

%build
%make CFLAGS="$RPM_OPT_FLAGS"
%make CFLAGS="$RPM_OPT_FLAGS" gui

%install
rm -rf $RPM_BUILD_ROOT

install -m755 %{name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m755 gtk%{name} -D $RPM_BUILD_ROOT%{_bindir}/gtk%{name}

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-gtkasp2php.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/gtk%{name}
Name=Asp2Php
Comment=Gtk frontend to asp2php
Icon=%{name}
Categories=X-MandrivaLinux-MoreApplications-Development-Tools;Development;
EOF

%if %mdkversion < 200900
%post -n gtkasp2php
%{update_menus}
%endif

%if %mdkversion < 200900
%postun -n gtkasp2php
%{clean_menus}
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc README LICENSE

%files -n gtkasp2php
%defattr(-,root,root)
%{_bindir}/gtk%{name}
#%{_libdir}/gtkasp2php/gtkasp2php
#%{_libdir}/gtkasp2php/*.xpm
#%{_libdir}/gtkasp2php/*.png
#%{_libdir}/gtkasp2php/asp2php
%{_datadir}/applications/mandriva-gtk%{name}.desktop
# icons
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.77.1-4mdv2011.0
+ Revision: 616607
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.77.1-3mdv2010.0
+ Revision: 423963
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.77.1-2mdv2009.0
+ Revision: 218429
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 11 2008 Thierry Vignaud <tv@mandriva.org> 0.77.1-2mdv2008.1
+ Revision: 165294
- fix description

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 0.77.1-1mdv2008.1
+ Revision: 142728
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 0.77.1-1mdv2007.0
+ Revision: 101611
- Import asp2php

* Wed May 24 2006 Emmanuel Andry <eandry@mandriva.org> 0.77.1-1mdk
- 0.77.1
- mkrel

* Wed Feb 02 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.76.23-1mdk
- 0.76.23

