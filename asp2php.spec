%define	name	asp2php
%define	version	0.77.1
%define	release	%mkrel 1


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

Install this if you intend to migrate from Microsuck, umm, I mean Micro$oft
(tm) Internet Information Server (tm) to PHP.

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

%post -n gtkasp2php
%{update_menus}

%postun -n gtkasp2php
%{clean_menus}


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


