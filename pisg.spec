Summary:	Perl script which generates statistics from IRC logfiles
Summary(pl):	Skrypt perlowy generuj�cy statystyki z plik�w loguj�cych IRC-a
Name:		pisg
Version:	0.64
Release:	0.9
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pisg/%{name}-%{version}.tar.gz
# Source0-md5:	e963b650c34b1e2c495d3e09897f59da
Patch0:		%{name}-config.patch
URL:		http://pisg.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pisg is an IRC channel statics generator written in Perl, it creates
statistics from different logfile formats. The supported logfile
formats is explained in the FORMATS file. It was originally written
because IRCStats wasn't open source. It's highly customizeable.
Extensive documentation can be found at:
<http://pisg.sourceforge.net/docs/>.

%description -l pl
pisg jest napisanym w Perlu generatorem statystyk kana�u IRC. Tworzy
je z r�nych format�w plik�w loguj�cych. Wspierane formaty s�
obja�nione w pliku FORMATS. Jest wysoko konfigurowalny. Obszerniejsza
dokumentacja znajduje si� na: <http://pisg.sourceforge.net/docs/>.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pisg,%{_datadir}/pisg,%{_bindir}}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
mv -f docs/pisg.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp pisg.cfg $RPM_BUILD_ROOT%{_sysconfdir}/pisg
cp -R gfx layout modules pisg lang.txt $RPM_BUILD_ROOT%{_datadir}/pisg
cat <<'EOF' > $RPM_BUILD_ROOT%{_bindir}/pisg
#!/bin/sh
exec %{_datadir}/pisg/pisg "$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs scripts
%dir %{_sysconfdir}/pisg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pisg/pisg.cfg
%dir %{_datadir}/pisg
%{_datadir}/pisg/gfx
%{_datadir}/pisg/layout
%{_datadir}/pisg/modules
%attr(755,root,root) %{_bindir}/pisg
%attr(755,root,root) %{_datadir}/pisg/pisg
%{_datadir}/pisg/lang.txt
%{_mandir}/man1/pisg*
