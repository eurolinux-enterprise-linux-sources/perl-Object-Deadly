Name:           perl-Object-Deadly
Version:        0.09
Release:        14%{?dist}
Summary:        Perl module providing an object that dies whenever examined
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Object-Deadly/
Source0:        http://search.cpan.org/CPAN/authors/id/J/JJ/JJORE/Object-Deadly-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp::Clan) >= 5.4
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Devel::Symdump)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Object::Deadly is meant to be used in testing. All possible
overloading and method calls die. You can pass this object into
methods which are not supposed to accidentally trigger any potentially
overloading.

%prep
%setup -q -n Object-Deadly-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Wed Oct 24 2012 Petr Pisar <ppisar@redhat.com> - 0.09-14
- Modernize spec file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.09-12
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 29 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-10
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-8
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.09-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.09-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.09-3
- rebuild for new perl

* Thu Oct 25 2007 Robin Norwood <rnorwood@redhat.com> - 0.09-2
- Fix BuildRequires

* Wed Oct 24 2007 Robin Norwood <rnorwood@redhat.com> - 0.09-1
- Initial build
