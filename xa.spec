#
# Conditional build:
%bcond_without	tests	# testing
#
Summary:	Cross-assembler for the 6502 and 65816 CPUs (and derivatives)
Summary(pl.UTF-8):	Asembler skrośny dla procesorów 6502 oraz 65816 (i pochodnych)
Name:		xa
Version:	2.4.1
Release:	1
License:	GPL v2+
Group:		Development/Languages
Source0:	https://www.floodgap.com/retrotech/xa/dists/%{name}-%{version}.tar.gz
# Source0-md5:	86ef6e8562b2e30b55c41e835178aede
Patch0:		%{name}-make.patch
URL:		https://www.floodgap.com/retrotech/xa/
%{?with_tests:BuildRequires:	perl-base}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-assembler for the 6502 and 65816 CPUs (and derivatives). xa is a
small, fast, portable two-pass assembler that compiles under most ANSI
C compilers.

%description -l pl.UTF-8
Asembler skrośny dla procesorów 6502 oraz 65816 (i pochodnych). Jest
to mały, szybki, przenośny, dwuprzebiegowy asembler, dający się
skompilować większością kompilatorów ANSI C.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	LD="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
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
