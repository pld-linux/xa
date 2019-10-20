#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	Cross-assembler for the 6502 and 65816 CPUs (and derivatives)
Name:		xa
Version:	2.3.9
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	https://www.floodgap.com/retrotech/xa/dists/%{name}-%{version}.tar.gz
# Source0-md5:	f533c3d36fcedcbca3b61a90ded6f37f
URL:		https://www.floodgap.com/retrotech/xa/
%{?with_tests:BuildRequires:	perl}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-assembler for the 6502 and 65816 CPUs (and derivatives). xa is a
small, fast, portable two-pass assembler that compiles under most ANSI
C compilers.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%{?with_tests:%{__make} -j1 test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.1st TODO
%attr(755,root,root) %{_bindir}/file65
%attr(755,root,root) %{_bindir}/ldo65
%attr(755,root,root) %{_bindir}/printcbm
%attr(755,root,root) %{_bindir}/reloc65
%attr(755,root,root) %{_bindir}/uncpk
%attr(755,root,root) %{_bindir}/xa
%{_mandir}/man1/file65.1*
%{_mandir}/man1/ldo65.1*
%{_mandir}/man1/printcbm.1*
%{_mandir}/man1/reloc65.1*
%{_mandir}/man1/uncpk.1*
%{_mandir}/man1/xa.1*
