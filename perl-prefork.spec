#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-prefork
Version  : 1.04
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/prefork-1.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AD/ADAMK/prefork-1.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libprefork-perl/libprefork-perl_1.04-2.debian.tar.xz
Summary  : 'Optimized module loading for forking or non-forking processes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0
Requires: perl-prefork-license
Requires: perl-prefork-man
Requires: perl(Module::Install::DSL)
BuildRequires : perl(Module::Install::DSL)

%description
NAME
prefork - Optimized module loading for forking or non-forking processes
SYNOPSIS
In a module that normally delays module loading with require

%package license
Summary: license components for the perl-prefork package.
Group: Default

%description license
license components for the perl-prefork package.


%package man
Summary: man components for the perl-prefork package.
Group: Default

%description man
man components for the perl-prefork package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n prefork-1.04
mkdir -p %{_topdir}/BUILD/prefork-1.04/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/prefork-1.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-prefork
cp LICENSE %{buildroot}/usr/share/doc/perl-prefork/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/prefork.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-prefork/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/prefork.3
