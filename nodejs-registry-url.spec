%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name registry-url

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        3.0.3
Release:        5%{?dist}
Summary:        Get the set npm registry URL
License:        MIT
URL:            https://github.com/sindresorhus/registry-url
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(require-uncached)
BuildRequires:  %{?scl_prefix}npm(mocha)
BuildRequires:  %{?scl_prefix}npm(rc)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%nodejs_fixdep rc

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%doc readme.md license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.3-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.3-4
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.3-3
- Enable find provides and requires macro

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.3-2
- Enable scl macros

* Fri Dec 18 2015 Troy Dawson <tdawson@redhat.com> - 3.0.3-1
- Update to 3.0.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-2
- Fix rc update dependency

* Sun Jan 25 2015 Parag Nemade <pnemade AT redhat DOT com> - 2.1.0-1
- update to 2.1.0 release

* Mon Dec 08 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-2
- Enabled tests

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.0-1
- Initial packaging