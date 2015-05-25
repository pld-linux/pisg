Summary:	Perl script which generates statistics from IRC logfiles
Summary(pl.UTF-8):	Skrypt perlowy generujący statystyki z plików logujących IRC-a
Name:		pisg
Version:	0.73
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pisg/%{name}-%{version}.tar.gz
# Source0-md5:	e0d43082c0bc20e19978743ebf2fcf8b
Patch0:		%{name}-config.patch
Patch1:		%{name}-FHS.patch
Patch2:		%{name}-lang.patch
Patch3:		%{name}-hacks.patch
Patch4:		no-autosilent.patch
URL:		http://pisg.sourceforge.net/
Suggests:	perl-Text-Iconv
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mv docs/pisg.1 .

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pisg,%{_datadir}/pisg,%{_bindir},%{_mandir}/man1,%{perl_vendorlib}}
cp -a pisg.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a pisg.cfg $RPM_BUILD_ROOT%{_sysconfdir}/pisg
cp -a gfx layout lang.txt $RPM_BUILD_ROOT%{_datadir}/pisg
cp -a modules/* $RPM_BUILD_ROOT%{perl_vendorlib}
install -p pisg $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/* scripts
%attr(755,root,root) %{_bindir}/pisg
%dir %{_sysconfdir}/pisg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pisg/pisg.cfg
%{perl_vendorlib}/Pisg.pm
%{perl_vendorlib}/Pisg
%dir %{_datadir}/pisg
%{_datadir}/pisg/gfx
%{_datadir}/pisg/layout
%{_datadir}/pisg/lang.txt
%{_mandir}/man1/pisg.1*
