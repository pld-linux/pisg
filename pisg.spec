Summary:	Perl script which generates statistics from IRC logfiles
Summary(pl):	-
Name:		pisg
Version:	0.64
Release:	0.9
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/pisg/%{name}-%{version}.tar.gz
# Source0-md5:	e963b650c34b1e2c495d3e09897f59da
Patch0:		%{name}-config.patch
URL:		http://pisg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pisg is an IRC channel statics generator written in Perl, it creates
statistics from different logfile formats. It was originally written
because IRCStats wasn't open source. So here's an open source/GPL'ed
version to anyone interested. It's a funny thing for your IRC channel,
and it's highly customizeable. Extensive documentation can be found
at: http://pisg.sourceforge.net/docs/

%description -l pl
-

%prep
%setup -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pisg,%{_datadir}/pisg,%{_bindir}}
cp pisg.cfg $RPM_BUILD_ROOT%{_sysconfdir}/pisg
cp -R gfx layout modules pisg lang.txt scripts $RPM_BUILD_ROOT%{_datadir}/pisg
echo '%{_datadir}/pisg/pisg $@' > $RPM_BUILD_ROOT%{_bindir}/pisg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs
%dir %{_sysconfdir}/pisg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pisg/pisg.cfg
%dir %{_datadir}/pisg
%{_datadir}/pisg/gfx
%{_datadir}/pisg/layout
%{_datadir}/pisg/modules
%{_datadir}/pisg/scripts
%attr(755,root,root) %{_bindir}/pisg
%attr(755,root,root) %{_datadir}/pisg/pisg
%{_datadir}/pisg/lang.txt
