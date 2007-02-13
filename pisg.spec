Summary:	Perl script which generates statistics from IRC logfiles
Summary(pl.UTF-8):	Skrypt perlowy generujący statystyki z plików logujących IRC-a
Name:		pisg
Version:	0.70
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pisg/%{name}-%{version}.tar.gz
# Source0-md5:	870c5ddf353c70d32159ac2dd310efc7
Patch0:		%{name}-config.patch
URL:		http://pisg.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pisg is an IRC channel statics generator written in Perl, it creates
statistics from different logfile formats. The supported logfile
formats is explained in the FORMATS file. It was originally written
because IRCStats wasn't open source. It's highly customizable.
Extensive documentation can be found at:
<http://pisg.sourceforge.net/docs/>.

%description -l pl.UTF-8
pisg jest napisanym w Perlu generatorem statystyk kanału IRC. Tworzy
je z różnych formatów plików logujących. Obsługiwane formaty są
objaśnione w pliku FORMATS. Jest wysoko konfigurowalny. Obszerniejsza
dokumentacja znajduje się na: <http://pisg.sourceforge.net/docs/>.

%prep
%setup -q
%patch0 -p1
mv docs/pisg.1 .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pisg,%{_datadir}/pisg,%{_bindir}}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install pisg.1 $RPM_BUILD_ROOT%{_mandir}/man1
install pisg.cfg $RPM_BUILD_ROOT%{_sysconfdir}/pisg
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
%attr(755,root,root) %{_bindir}/pisg
%dir %{_sysconfdir}/pisg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pisg/pisg.cfg
%dir %{_datadir}/pisg
%{_datadir}/pisg/gfx
%{_datadir}/pisg/layout
%{_datadir}/pisg/modules
%attr(755,root,root) %{_datadir}/pisg/pisg
%{_datadir}/pisg/lang.txt
%{_mandir}/man1/pisg*
